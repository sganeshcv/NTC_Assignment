import numpy as np
import math
import sys
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
    cipherText = "EYATGNACOHETKNTMTSIZ"
    factors = getfactors(len(cipherText))
    for factor in factors:
        plainText = decrypt(cipherText.lower(),factor)
        print(plainText) #op

if __name__ == "__main__":
    main()