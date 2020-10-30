from heapq import nlargest 

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
TOTAL_CHARACTERS = 4374127904

MONOGRAM_FILE = '/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Shift/cryptanalysis/english-monograms.txt'
# BIGRAM_FILE = 'english-bigrams.txt'
# TRIGRAM_FILE = 'english-trigrams.txt'
# QUADGRAM_FILE = 'english-quadgrams.txt'

def mod26(num):
    return (num%26)

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

def main():
    message = "XLILSYWIMWRSAJSVWEPIJSVJSYVQMPPMSRHSPPEVWMXMWASVXLQSVILYVVCFIJSVIXLIWIPPIVVIGIMZIWQSVISJJIVW"  #gt pt
    print(message)
    actual_frequency_distribution = readNGram(1)
    ciphertext_frequency_distribution = determineFrequencyDistribution(message.lower())
    # print(actual_frequency_distribution)
    # print(ciphertext_frequency_distribution)
    frequent_char_actual = max(actual_frequency_distribution,key=actual_frequency_distribution.get)
    frequent_char3 = nlargest(3, ciphertext_frequency_distribution, key=ciphertext_frequency_distribution.get)
    for frequent_char in frequent_char3:
        key = getKey(frequent_char_actual, frequent_char)
        print("{} : {}".format(CHARACTERS[key], decrypt(key,message)))
        #break

if __name__ == "__main__":
    main()