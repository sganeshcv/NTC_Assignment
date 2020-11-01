import sys

file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Vigenere/cryptanalysis/knownPT/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Vigenere/cryptanalysis/knownPT/output.txt"

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def mod26(num):
    return (num%26)

def setKey(key,message):
    while len(key) < len(message):
        key += key
    return key

def getKey(char1, char2):
    return mod26(int(CHARACTERS.upper().find(char1)) - int(CHARACTERS.find(char2)))

def findKey(key_length,plain_text,cipher_text):
    key = ''
    i = 0
    while i < key_length :
        key += CHARACTERS[getKey(cipher_text[i],plain_text[i])]
        i += 1
    return key

def main():
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.find("plain_text") != -1:    
                plain_text = (line.rstrip('\n').split(" = ")[1])
            elif line.find("cipher_text") != -1:
                cipher_text = (line.rstrip('\n').split(" = ")[1])
            elif line.find("key_length") != -1:
                key_length = int(line.rstrip('\n').split(" = ")[1])
    
    fout = open(file_output, "w+")
    key = findKey(key_length,plain_text,cipher_text)
    print(key)
    fout.write(key)

if __name__ == "__main__":
    main()