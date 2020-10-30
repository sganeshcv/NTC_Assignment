from heapq import nlargest 
# from sage import *
import numpy as np

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
TOTAL_CHARACTERS = 4374127904

KEYDOMAIN = [ 1,  3,  5,  7,  9,  11,  15,  17,  19,  21,  23,  25 ]  #key domain for key1

file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Affine/cryptanalysis/statistic/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Affine/cryptanalysis/statistic/output.txt"
MONOGRAM_FILE = '/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Affine/cryptanalysis/english-monograms.txt'
# BIGRAM_FILE = 'english-bigrams.txt'
# TRIGRAM_FILE = 'english-trigrams.txt'
# QUADGRAM_FILE = 'english-quadgrams.txt'

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

def determineFrequencyDistribution(ciphertext):
    total = 0    
    letter_count = {}
    for letter in ciphertext:
        if letter in CHARACTERS:
            if letter in letter_count.keys():
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
            total += 1

    frequency_distribution = {}
    for letter in letter_count:
        frequency_distribution[letter] = (letter_count[letter] / total) * 100
    
    for letter in CHARACTERS:
        if letter not in frequency_distribution.keys():
            frequency_distribution[letter] = 0
    return frequency_distribution    

def readNGram(depth):
    frequency_distribution = {}                
    # Monogram
    if depth == 1:
        with open(MONOGRAM_FILE, 'r') as mf:
            for line in mf.readlines():
                tokens = line.split()
                key = str(tokens[0]).lower()
                frequency = (int(tokens[1]) / TOTAL_CHARACTERS) * 100
                frequency_distribution[key] = frequency
    return frequency_distribution

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
            if line.lower().find("message") != -1:    
                message = line.rstrip('\n').split(" = ")[1]

    fout = open(file_output, "w+")
    
    actual_frequency_distribution = readNGram(1)
    ciphertext_frequency_distribution = determineFrequencyDistribution(message.lower())
    
    frequent_chars_actual = nlargest(2,actual_frequency_distribution,key=actual_frequency_distribution.get)
    frequent_chars_cipher = nlargest(2, ciphertext_frequency_distribution, key=ciphertext_frequency_distribution.get)
    
    matrix_A = [[CHARACTERS.find(frequent_chars_actual[0]), 1], [CHARACTERS.find(frequent_chars_actual[1]), 1]]
    matrix_B = [[CHARACTERS.find(frequent_chars_cipher[0])],[CHARACTERS.find(frequent_chars_cipher[1])]]
    matrix_key = np.dot(mod26MatInv(matrix_A),matrix_B)
    key1 = int(mod(matrix_key)[0])
    key2 = int(mod(matrix_key)[1])
    if key1 in KEYDOMAIN:
        print("Key1 : {} \nKey2 : {}".format(key1,key2))
        fout.write("Key1 : {} \nKey2 : {}\n".format(key1,key2))
        #break
    else :
        print("An error occured")

    print(decrypt([key1,key2],message))
    fout.write(decrypt([key1,key2],message))

if __name__ == "__main__":
    main()