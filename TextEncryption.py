from cisc108 import assert_equal
"""
Goal of project is to build some simple functions that encrypt, decrypt, and hash text
for cryptography purposes.
"""

# 1) Define helper_functions

# 1-1 Define ord helper
def ordinal(string: str) -> [int]:
    """
    This function takes a string of characters and converts it to
    its ordianal value and returns it as a list if integers.
    
    Args:
        string str: a string of characters.
    Returns:
        a list of integers.
    """
    new_list = []
    ord_list = []
    for a_character in string:
        new_list.append(a_character)
    for a_list in new_list:
        ord_list.append(ord(a_list))
    return ord_list

# 1-2 Define chr helper
def character(num_list:[int]) -> str:
    """
    This function takes a list of integers and converts it to a
    string of characters.
    
    Args:
        num_list [int]: takes a list of integers.
    Returns:
        a string of characters.
    """
    new_string = ''
    for number in num_list:
        new_string = new_string + (chr(number))
    return new_string

# 1-3 Define rotate helper
def rotate(rotate_list:[int], rotate_num:int) -> [int]:
    """
    This function takes a list of integers to be rotated and the number
    of how many rotations it will do.
    
    Args:
        rotate_list [int]: the inputed list of integers to be rotated.
        rotate_num int: the number of times each integer in the rotate_list
        will be rotated.
    Returns:
        the list of rotated numbers 
    """
    new_list = []
    for element in rotate_list:
        new_list.append(element + rotate_num)
    return new_list

# 2) Define encrypt_text
def encrypt_algorithm(message:str, rotate_amount:int) -> str:
    """
    Takes the inputed str to be turned into its ordinal value. It then
    uses the rotation formula to rotate each ordinal value of a character.
    IT then checks if the number is less then 48, and if True then appends
    126 to the end of the number. it then converts the list of integers back to
    characters, but encrypted.
    
    Args:
        message str: a str that is going to be encrypted using the encryption formula
        rotate_amount int: the number of times each integer in a list is going to be rotated
    Returns:
        a rotated str of characters.
    """
    new_number = []
    final_list = []
    message = ordinal(message)
    for a_character in message:
        new_number.append((a_character + rotate_amount - 32) % 94 + 32)
    for num in new_number:
        final_list.append(num)
        if num < 48:            
            final_list.append(126)
    return character(final_list)

# 3) Define decrypt_text
def decrypt_algorithm(message:str, rotate_amount:int) -> [int]:
    """
    Takes a input of a string that was previously encrypted and is inputed into the message variable.
    it then takes a previously established rotation amount and subtracts it back to the previous number. It then goes
    through the character function and turns in back into a character in a string.
    
    Args:
        message str: takes a previously encrypted message as a str.
        rotate_amount int: takes a previously established rotation amount.
    Returns:
        a rotated listed of integers that run through the character function and
        converts them to characters in a string.
        
    """
    new_list = []
    rotate_list = []
    message = ordinal(message)
    for a_number in message:
        if a_number != 126:
            new_list.append(a_number)
            rotate_list.append((a_number - rotate_amount - 32) % 94 + 32)
    return character(rotate_list) 
    
# 4) Define hash_text
def hash_algorithm(message:str, base_value:int, hash_size: int) -> [int]:
    """
    Takes a message to be encrypted or a message to be decrypted and adds a given
    base value and put it to what power the ordinal value of a character.
    
    Args:
        message str: message to be converted to a hash value
        base_value int: the base value being put to the power of the ordinal value of each character in message parameter.
        hash_size int: size of hash value
    Returns:
        a list of each ordianl value of a characher ran through the hash formula.
    """
    final_list = []
    sum = 0
    new_list = ordinal(message)
    for index, a_number in enumerate(new_list):
        final_list.append(((index) + base_value) ** a_number)
    for a_number in final_list:
        sum = sum + a_number
    hash_value = sum % hash_size
    return hash_value

# 5) Define main
def main():
    """
    
    """
    answer = input("Would you like to encrypt (E) or decrypt (D) a message?: ")
    answer = answer.upper()
    if answer == "E":
        message = input("Write the message you want to encrpyt: ")
        encrypt_message = encrypt_algorithm(message,5)
        hash_num = hash_algorithm(message,31,1000000000)
        print("Encrypted message:",encrypt_message)
        print("Hash value:",hash_num)
    elif answer == "D":
        message = input("Write the message you want to decrypt: ")
        decrypt_message = decrypt_algorithm(message,5)
        hash_num = input("Write your hashing value: ")
        if int(hash_num) == hash_algorithm(decrypt_message, 31, 1000000000):
            print("Decrypted message:",decrypt_message)
        else:
            print("error")
    else:
        return print("error")

main()

# ordinal function
"""
print("\nORDINAL FUNCTION:")
assert_equal(ordinal("Hello World!"), [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33])
assert_equal(ordinal("My name is Michael Lorang"), [77, 121, 32, 110, 97, 109, 101, 32, 105, 115, 32, 77, 105, 99, 104, 97, 101, 108, 32, 76, 111, 114, 97, 110, 103])
assert_equal(ordinal("I love corgis"), [73, 32, 108, 111, 118, 101, 32, 99, 111, 114, 103, 105, 115])

# character function
print("\nCHARACTER FUNCTION:")
assert_equal(character([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]), "Hello World!")
assert_equal(character([77, 121, 32, 110, 97, 109, 101, 32, 105, 115, 32, 77, 105, 99, 104, 97, 101, 108, 32, 76, 111, 114, 97, 110, 103]), "My name is Michael Lorang")
assert_equal(character([73, 32, 108, 111, 118, 101, 32, 99, 111, 114, 103, 105, 115]), "I love corgis")

# rotate function
print("\nROTATE FUNCTION:")
assert_equal(rotate([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33], 5), [77, 106, 113, 113, 116, 37, 92, 116, 119, 113, 105, 38])
assert_equal(rotate([77, 121, 32, 110, 97, 109, 101, 32, 105, 115, 32, 77, 105, 99, 104, 97, 101, 108, 32, 76, 111, 114, 97, 110, 103], 5), [82, 126, 37, 115, 102, 114, 106, 37, 110, 120, 37, 82, 110, 104, 109, 102, 106, 113, 37, 81, 116, 119, 102, 115, 108])
assert_equal(rotate([73, 32, 108, 111, 118, 101, 32, 99, 111, 114, 103, 105, 115], 5), [78, 37, 113, 116, 123, 106, 37, 104, 116, 119, 108, 110, 120])

# encrypt_algorithm function
print("\nENCRYPT_ALGORITHM FUNCTION:")
assert_equal(encrypt_algorithm("Hello World!", 5), "Mjqqt%~\\twqi&~")
assert_equal(encrypt_algorithm("My name is Michael Lorang", 5), "R ~%~sfrj%~nx%~Rnhmfjq%~Qtwfsl")
assert_equal(encrypt_algorithm("I love corgis", 5), "N%~qt{j%~htwlnx")

# decrypt_algorithm function
print("\nDECRYPT_ALGORITHM FUNCTION:")
assert_equal(decrypt_algorithm("Mjqqt%~\\twqi&~", 5), "Hello World!")
assert_equal(decrypt_algorithm("R ~%~sfrj%~nx%~Rnhmfjq%~Qtwfsl", 5), "My name is Michael Lorang")
assert_equal(decrypt_algorithm("N%~qt{j%~htwlnx", 5), "I love corgis")

# hash_algorithm function
print("\nHASH_ALOGRITHM FUNCTION:")
assert_equal(hash_algorithm("Hello World!", 31, 1000000000), 811478700)
assert_equal(hash_algorithm("My name is Michael Lorang" , 31, 1000000000), 198391187)
assert_equal(hash_algorithm("I love corgis" , 31, 1000000000), 278903485)
"""