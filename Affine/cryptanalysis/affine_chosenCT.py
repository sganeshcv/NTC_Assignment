from heapq import nlargest 
# from sage import *
import numpy as np

file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Affine/cryptanalysis/chosenCT/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Affine/cryptanalysis/chosenCT/output.txt"

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

KEYDOMAIN = [ 1,  3,  5,  7,  9,  11,  15,  17,  19,  21,  23,  25 ]  #key domain for key1


def mod(num):
    return (num%26)

def modInverse(num): 
    m = len(CHARACTERS)
    num = num % m
    for x in range(1, m) : 
        if ((num * x) % m == 1): 
            return x 
    return 1

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

def decrypt(keys,message):
    plainText = ''
    for character in message:
        if character in CHARACTERS.upper():
            character_index = CHARACTERS.upper().find(character)
            plainText += CHARACTERS[mod((character_index - keys[1]) * modInverse(keys[0]))]
        else:
            plainText += character
    return plainText

def main():
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.lower().find("message") != -1:    # if case-insensitive match,
                message = line.rstrip('\n').split(" = ")[1]
            elif line.find("chosen_cipherText") != -1:
                chosen_cipherText = line.rstrip('\n').split(" = ")[1]
            elif line.find("PlainText_corresponding_to_CT1") != -1:
                PlainText_corresponding_to_CT1 = line.rstrip('\n').split(" = ")[1]
            elif line.find("PlainText_corresponding_to_CT2") != -1:
                PlainText_corresponding_to_CT2 = line.rstrip('\n').split(" = ")[1]
      
    fout = open(file_output, "w+")
    
    matrix_A = [[CHARACTERS.upper().find(chosen_cipherText[0])], [CHARACTERS.upper().find(chosen_cipherText[1])]]
    matrix_B = [[CHARACTERS.find(PlainText_corresponding_to_CT1[0]), 1],[CHARACTERS.find(PlainText_corresponding_to_CT1[1]), 1]]
    matrix_C = [[CHARACTERS.find(PlainText_corresponding_to_CT2[0]), 1],[CHARACTERS.find(PlainText_corresponding_to_CT2[1]), 1]]
    matrix_key1 = np.dot(mod26MatInv(matrix_B),matrix_A)
    matrix_key2 = np.dot(mod26MatInv(matrix_C),matrix_A)
    key11 = int(mod(matrix_key1)[0])
    key21 = int(mod(matrix_key1)[1])
    key12 = int(mod(matrix_key2)[0])
    key22 = int(mod(matrix_key2)[1])
    if key11 in KEYDOMAIN:
        print("Key1 : {} \nKey2 : {}".format(key11,key21))
        fout.write(str("Key1 : {} \nKey2 : {}\n".format(key11,key21)))
        print(decrypt([key11,key21],message))
        fout.write(decrypt([key11,key21],message))
        #break
    elif key12 in KEYDOMAIN:
            print("Key1 : {} \nKey2 : {}".format(key12,key22))
            fout.write(str("Key1 : {} \nKey2 : {}\n".format(key12,key22)))
            print(decrypt([key12,key22],message))
            fout.write(decrypt([key12,key22],message))
    else:
        print("An error occured")

if __name__ == "__main__":
    main()