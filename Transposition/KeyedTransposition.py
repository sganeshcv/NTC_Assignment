import sys

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def messageValidation(message):
    for key in message:
        if  key not in CHARACTERS:
            sys.exit("The key should be greater than or equal to zero!!")

def setUpMessage(message,m):
    nearest_int = int(len(message)/m)
    new_message_length = (nearest_int + 1)*m
    i = 0
    while i < (int(new_message_length - len(message))):
        message += "z"
        i += 1
    return message

def shuffle(part_message,key):
    new_message = ""
    for i in range(len(key)):
        new_message += part_message[key[i]-1]
    return new_message

def deshuffle(part_message,key):
    new_message = ""
    for i in range(len(key)):
        index_char = key.index(i+1)
        new_message += part_message[index_char]
    return new_message

def encrypt(keys,message):
    cipherText = ''
    i = 0
    while i < len(message):
            cipherText += shuffle(message[i:i+len(keys)],keys)
            i += len(keys)
    return cipherText

def decrypt(keys,message):
    plainText = ''
    i = 0
    while i < len(message):
            plainText += deshuffle(message[i:i+len(keys)],keys)
            i += len(keys)
    return plainText

def main():
    message = "enemyattackstonight"  #gt pt
    key = [3, 1, 4, 5, 2]         #gtkeys
    messageValidation(message)
    message = setUpMessage(message,len(key))
    cipherText = encrypt(key,message)
    print(cipherText)
    plainText = decrypt(key,cipherText)
    print(plainText) 

if __name__ == "__main__":
    main()