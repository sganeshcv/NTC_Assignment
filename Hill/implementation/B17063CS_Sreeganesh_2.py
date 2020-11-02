import numpy as np
import math
import sys

file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Hill/implementation/Hill/B17063CS_Sreeganesh_2_I.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Hill/implementation/Hill/B17063CS_Sreeganesh_2_O.txt"

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def mod26(num):
    return (num%26)

def setUpMessage(message, m):
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

def getMatrix(message,m):
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

def encrypt(key,message,m):
  keyMatrix = key#getMatrix(key)
  messageVector = getMatrix(message,m)     # numberize
  cipherMatrix = np.dot(messageVector,keyMatrix)
  return getText(cipherMatrix)

def decrypt(key, message,m):
  keyMatrix = key#keyMatrix = getMatrix(key)
  keyMatrixInverse = mod26MatInv(keyMatrix)
  messageVector = getMatrix(message,m)
  plainText = np.dot(messageVector,keyMatrixInverse)
  return getText(plainText)

def main():
  with open (file_input, 'rt') as myfile:
      for line in myfile:
          if line.find("key_dimension") != -1:    
              key_dimension = int(line.rstrip('\n').split(" = ")[1])
          elif line.find("key") != -1:
              key_text = (line.rstrip('\n').split(" = ")[1])
          elif line.find("message") != -1:
              message = (line.rstrip('\n').split(" = ")[1])
  fout = open(file_output, "w+")
  key = getMatrix(key_text,key_dimension)
  modified_message = setUpMessage(message,key_dimension)
  cipherText = encrypt(key,modified_message,key_dimension)
  print(cipherText.upper())
  fout.write(cipherText.upper())
  fout.write("\n")
  plainText = decrypt(key,cipherText,key_dimension)
  print(plainText)
  fout.write(plainText)
    
if __name__ == "__main__":
  main()