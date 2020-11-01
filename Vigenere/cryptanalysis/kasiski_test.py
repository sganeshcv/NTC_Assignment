import sys
from fractions import gcd
from functools import reduce

file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Vigenere/cryptanalysis/kasiski_test/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Vigenere/cryptanalysis/kasiski_test/output.txt"


TOTAL_CHARACTERS = 4374127904
CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
MONOGRAM_FILE = '/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Shift/cryptanalysis/english-monograms.txt'

def mod26(num):
    return (num%26)

def find_gcd(list):
    x = reduce(gcd, list)
    return x

def getSplit(message):
    occurences = {}
    for i in range(0,len(message)-3):
        occurences[message[i:i+3]] = [j for j in range(len(message)) if message.startswith(message[i:i+3], j)]
    occurence_list = [k for k in occurences.keys() if len(occurences[k]) > 1]
    print(occurence_list)
    difference = []
    for k in occurence_list:
        values = list(occurences[k])
        difference.append(values[1] - values[0])
    return find_gcd(difference)

def setSplitSentences(split, message):
    split_sentenses = {}
    for i in range(split) :
        split_sentenses[i] = ""
    i = 0
    while i < len(message):
        for j in range(0,split):
            if i+j < len(message):
                split_sentenses[j] += message[i+j]
        i += split
    return split_sentenses


def getKey(c1, c2):
    return mod26(CHARACTERS.find(c2) - CHARACTERS.find(c1))

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

def decrypt(key,message):
    plainText = ''
    for character in message:
        if character in CHARACTERS.upper():
            character_index = CHARACTERS.upper().find(character)
            plainText += CHARACTERS[mod26(character_index - key)]
        else:
            plainText += character
    return plainText

def decryptBruteForce(key,message):
    plainText = ''
    for character in message:
        if character in CHARACTERS.upper():
            character_index = CHARACTERS.upper().find(character)
            plainText += CHARACTERS[mod26(character_index - key)]
        else:
            plainText += character
    return plainText

def printDecryptedMessage(split,split_sentenses,max_len):
    message = ""
    i = 0
    l = 0
    while(i < max_len):
        for j in range(split):
            if(l < len(split_sentenses[j])):
                message += split_sentenses[j][l]
        i += split
        l += 1
    return message

def main():
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.find("message") != -1:    
                message = (line.rstrip('\n').split(" = ")[1])

    fout = open(file_output, "w+")    
    split = getSplit(message)
    max_len = len(message)
    split_sentenses = setSplitSentences(split,message)
    print(split_sentenses)
    decrypt_messages = []
    for message in list(split_sentenses.values()):
        actual_frequency_distribution = readNGram(1)
        ciphertext_frequency_distribution = determineFrequencyDistribution(message.lower())
        frequent_char_actual = max(actual_frequency_distribution,key=actual_frequency_distribution.get)
        frequent_char_cipher = max(ciphertext_frequency_distribution, key=ciphertext_frequency_distribution.get)
        key = getKey(frequent_char_actual, frequent_char_cipher)
        decrypt_messages.append(decrypt(key,message))
        print("{} : {}".format(CHARACTERS[key], decrypt(key,message)))
    print("Here statistical attack didn't work on the last part so we can do a bruteforce instead")
    message = list(split_sentenses.values())[3]  #gt pt
    print(message)
    last_part = []
    for key in range(1,26):
        plainText = decryptBruteForce(key,message)
        print("{} : {}".format(key, plainText))
        last_part.append(plainText)
    for last_text in last_part:
        decrypt_messages.pop()
        decrypt_messages.append(last_text)
        print(printDecryptedMessage(split,decrypt_messages,max_len))
        fout.write(printDecryptedMessage(split,decrypt_messages,max_len)+ "\n")


    print("Now we can clearly see the actual plaintext from the above list")
if __name__ == "__main__":
    main()