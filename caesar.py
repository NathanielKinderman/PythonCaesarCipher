"""
Python program is created to simulate a Caesar Ciper encryption/decryption text
"""

VALID_STRING = "abcdefghijklmnopqrstuvwxyz"

def encryption(text,key):
    #takes text and encrypt it by multiply the text by 2

    encrypt_string = 'abcdefghiklmnopqrstuvwxyz' * 2 
    output = ''

    for char in VALID_STRING:
        if char in VALID_STRING:
            index = encrypt_string.index(str(char))
            output += encrypt_string[index + key]
        else:
            output += char
    return output