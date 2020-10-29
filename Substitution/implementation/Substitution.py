import sys

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def keyValidation(key):
    if  key not in CHARACTERS:
        sys.exit("The key should be greater than or equal to zero!!")

def encrypt(keys,message):
    cipherText = ''
    for character in message :
        if character in CHARACTERS:
            character_index = CHARACTERS.find(character)
            cipherText += keys[character_index].upper()
        else:
            cipherText += character
    return cipherText

def decrypt(keys,message):
    plainText = ''
    for character in message:
        if character in CHARACTERS.upper(): 
            character_index = keys.upper().find(character)
            plainText += CHARACTERS[character_index]
        else:
            plainText += character
    return plainText

def main():
    message = "abcdefga"  #gt pt
    key = "keyabcdfghijlmnopqrstuvwxz"         #gtkeys
    cipherText = encrypt(key,message)
    print(cipherText)
    plainText = decrypt(key,cipherText)
    print(plainText) 

if __name__ == "__main__":
    main()