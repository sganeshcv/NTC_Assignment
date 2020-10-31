import numpy as np
import math
import sys

file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Transposition/cryptanalysis/BruteForce/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Transposition/cryptanalysis/BruteForce/output.txt"

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"  

def getfactors(n):
    factors = []
    i = 1
    while i <= n : 
        if (n % i==0) : 
            factors.append(i)
        i += 1
    return factors

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

def decrypt(message,m):
    message_Matrix = getMatrixDecrypt(message,m)
    return getText(message_Matrix)

def main():
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.find("cipherText") != -1:    
                cipherText = (line.rstrip('\n').split(" = ")[1])
    
    fout = open(file_output, "w+")    
    factors = getfactors(len(cipherText))
    for factor in factors:
        plainText = decrypt(cipherText.lower(),factor)
        print(plainText) #op
        fout.write(plainText)
        fout.write("\n")

if __name__ == "__main__":
    main()