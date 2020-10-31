import numpy as np
import math
import sys

file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Transposition/implementation/keylessTransposition/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Transposition/implementation/keylessTransposition/output.txt"

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

def getMatrixEncrypt(message,m):   
    coloumn = m
    row = int(len(message)/m)
    keyMatrix = np.zeros((row,coloumn)) #numberize
    c = 0
    for i in range(row):
        for j in range(coloumn):
            keyMatrix[i][j] = CHARACTERS.find(message[c])
            c += 1
    return keyMatrix

def getMatrixDecrypt(message,m):   
    coloumn = m
    row = int(len(message)/m)
    keyMatrix = np.zeros((row,coloumn)) #numberize
    c = 0
    for i in range(coloumn):
        for j in range(row):
            keyMatrix[j][i] = CHARACTERS.find(message[c])
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

def encrypt(message,m):
    modified_message = setUpMessage(message,m)
    message_Matrix = getMatrixEncrypt(modified_message,m)
    return getText(message_Matrix.transpose())

def decrypt(message,m):
    message_Matrix = getMatrixDecrypt(message,m)
    return getText(message_Matrix)

def main():
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.find("coloumn_length") != -1:    
                m = int(line.rstrip('\n').split(" = ")[1])
            elif line.find("message") != -1:
                message = (line.rstrip('\n').split(" = ")[1])
    fout = open(file_output, "w+")
    cipherText = encrypt(message,m)
    print(cipherText.upper())
    fout.write(cipherText.upper() + "\n")
    plainText = decrypt(cipherText,m)
    print(plainText)
    fout.write(plainText)

if __name__ == "__main__":
    main()