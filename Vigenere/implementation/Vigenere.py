import sys

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def mod26(num):
    return (num%26)

def setKey(key,message):
    keys = key
    for i in range(0,len(message)-1):
        keys += message[i]
    return keys

def encrypt(keys,message):
    cipherText = ''
    for (character,i) in zip(message,range(0,len(keys))):
        if character in CHARACTERS:
            character_index = CHARACTERS.find(character)
            key_indeex = CHARACTERS.find(keys[i])
            cipherText += CHARACTERS[mod26(character_index + key_indeex)].upper()
        else:
            cipherText += character
    return cipherText

def decrypt(keys,message):
    plainText = ''
    for (character,i) in zip(message,range(0,len(keys))):
        if character in CHARACTERS.upper(): 
            character_index = CHARACTERS.upper().find(character)
            key_index = CHARACTERS.find(keys[i])
            plainText += CHARACTERS[mod26(character_index - key_index)]
        else:
            plainText += character
    return plainText
            

def keyValidation(key):
    if  key not in CHARACTERS:
        sys.exit("The key should be greater than or equal to zero!!")

def main():
    message = "abcdefga"  #gt pt
    key0 = "a"         #gtkeys
    keyValidation(key0)
    key = setKey(key0,message)
    cipherText = encrypt(key,message)
    print(cipherText)
    plainText = decrypt(key,cipherText)
    print(plainText) 

if __name__ == "__main__":
    main()