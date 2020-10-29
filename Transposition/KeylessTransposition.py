import numpy as np
import math
import sys
CHARACTERS = "abcdefghijklmnopqrstuvwxyz"  

def setUpMessage(message,m):
    if len(message)%m == 0:
        return message
    message_length = len(message)
    nearest_int = int(message_length/m)
    new_message_length = (nearest_int + 1)*m
    i = 0
    while i < (int(new_message_length - message_length)):
        message += "z"
        i += 1
    return message

def getMatrix(message,m):   
    coloumn = m
    row = m
    keyMatrix = np.zeros((row,coloumn)) #numberize
    c = 0
    for i in range(row):
        for j in range(coloumn):
            keyMatrix[i][j] = CHARACTERS.find(message[c])
            c += 1
    return keyMatrix

def getText(message):
    messgaeText = ""
    row = message.shape[0]
    coloumn = message.shape[1]
    for i in range(row):
        for j in range(coloumn):
            messgaeText += CHARACTERS[int(message[i][j])]
    return messgaeText

def encryptdecrypt(message,m):
    modified_message = setUpMessage(message,m*m)
    i = 0
    cipherText = ""
    while i < len(modified_message):
        message_Matrix = getMatrix(modified_message[i:i+(m*m)],m)
        cipherText += getText(message_Matrix.transpose())
        i += m*m
    return cipherText

def main():
    #get key dimensions
    m = 4
    message = "wearethechampionsoftheworld"    #get message
    cipherText = encryptdecrypt(message,m)
    print(cipherText)
    plainText = encryptdecrypt(cipherText,m)
    print(plainText)
    
if __name__ == "__main__":
    main()