import sys

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def mod26(num):
    return (num%26)


def encrypt(key,message):
    cipherText = ''
    for character in message:
        if character in CHARACTERS:
            character_index = CHARACTERS.find(character)
            cipherText += CHARACTERS[mod26(character_index + key)].upper()
        else:
            cipherText += character
    return cipherText

def decrypt(key,message):
    plainText = ''
    for character in message:
        if character in CHARACTERS.upper():
            character_index = CHARACTERS.upper().find(character)
            plainText += CHARACTERS[mod26(character_index - key)]
        else:
            plainText += character
    return plainText
            

def keyValidation(key):
    if  key < 0:
        sys.exit("The key should be greater than or equal to zero!!")

def main():
    message = "thehouseisnowforsaleforfourmilliondollarsitisworthmorehurrybeforethesellerreceivesmoreoffers"  #gt pt
    key = 4         #gtkeys
    keyValidation(key)
    cipherText = encrypt(key,message)
    print(cipherText)
    plainText = decrypt(key,cipherText)
    print(plainText) 

if __name__ == "__main__":
    main()