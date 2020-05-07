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


def decryption(text,key):
    #decrypts texts that have beem encrypted

    decrypt_string='zyxwvutsrqponmlkihgfedcba'
    output = ''
    
    for char in text:
        if char in VALID_STRING:
            index = decrypt_string.index(str(char))
            output += decrypt_string[index+key]
        else:
            output += char
    return output


if __name__ == '__main__':

    print( 
    """
    1. Press 1 to Encrypt text \n
    2. Press 2 to Decrypt text \n
    3. Press 3 to do both \n
    """)
    choice = input('Enter a choice: ')
        
    if choice == 1:
        input_txt = raw_input('Enter the text to encrypt:')
        key       = input('Enter Key between 1 to 25 :')
        print ("The encrypted text is : ")
        print encryption(input_txt, key)
        
    elif choice == 2:
        input_txt = raw_input('Enter the text to decrypt:')
        key       = input('Enter Key between 1 to 25 :')
        print "The decrypted text is : "
        print decryption(input_txt, key)

    elif choice == 3:
        input_txt = raw_input('Enter the text:')
        key       = input('Enter Key between 1 to 25 :')
        
        print "The encrypted text is : "
        print encryption(input_txt, key)
        
        print "The decrypted text is : "
        print decryption(input_txt, key)
    else:
        print 'Invalid choice'