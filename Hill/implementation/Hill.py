import numpy as np
import math
import sys
CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

m = 4
def mod26(num):
    return (num%26)

def setUpMessage(message):
    message_length = len(message)
    nearest_int = int(message_length/m)
    new_message_length = (nearest_int + 1)*m
    i = 0
    while i < (int(new_message_length - message_length)):
        message += "z"
        i += 1
    return message


def mod26MatInv(A):       # Finds the inverse of matrix A mod p
  n = len(A)
  p = 26
  A=np.matrix(A)
  adj=np.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(np.linalg.det(minor(A,j,i)))))%p
  return (modInv(int(round(np.linalg.det(A))),p)*adj)%p

def modInv(a,p):          # Finds the inverse of a mod p, if it exists
  for i in range(1,p):
    if (i*a)%p==1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(p))

def minor(A,i,j):    # Return matrix A with the ith row and jth column deleted
  A=np.array(A)
  minor=np.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor


def getMatrix(message):
    coloumn = m
    row = int(len(message)/m)
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
            messgaeText += CHARACTERS[mod26(int(message[i][j]))]
    return messgaeText


def encrypt(key,message):
    keyMatrix = key#getMatrix(key)
    messageVector = getMatrix(message)     # numberize
    cipherMatrix = np.dot(messageVector,keyMatrix)
    return getText(cipherMatrix)



def decrypt(key, message):
    keyMatrix = key#keyMatrix = getMatrix(key)
    keyMatrixInverse = mod26MatInv(keyMatrix)
    messageVector = getMatrix(message)
    plainText = np.dot(messageVector,keyMatrixInverse)
    return getText(plainText)



def main():
    #get key dim
    key = [[9, 7, 11, 13], [4, 7, 5, 6], [2, 21, 14, 9], [3, 23, 21, 8]]#get key
    message = "codeisready"#get message
    modified_message = setUpMessage(message)
    print(modified_message)
    cipherText = encrypt(key,modified_message)
    print(cipherText)
    plainText = decrypt(key,cipherText)
    print(plainText)
    
if __name__ == "__main__":
    main()
