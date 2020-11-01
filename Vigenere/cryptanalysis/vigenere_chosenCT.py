import sys

file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Vigenere/cryptanalysis/chosenCT/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Vigenere/cryptanalysis/chosenCT/output.txt"

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

def decrypt(keys,message):
    plainText = ''
    for (character,i) in zip(message,range(0,len(message))):
        if character in CHARACTERS.upper(): 
            character_index = CHARACTERS.upper().find(character)
            key_index = CHARACTERS.find(keys[i])
            plainText += CHARACTERS[mod26(character_index - key_index)]
        else:
            plainText += character
    return plainText

def main():
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.lower().find("message") != -1:    # if case-insensitive match,
                message = line.rstrip('\n').split(" = ")[1]
            elif line.find("cipher_text") != -1:    
                cipher_text = (line.rstrip('\n').split(" = ")[1])
            elif line.find("plain_text1") != -1:
                plain_text1 = (line.rstrip('\n').split(" = ")[1])
            elif line.find("plain_text2") != -1:
                plain_text2 = (line.rstrip('\n').split(" = ")[1])
    
    plain_texts = [plain_text1, plain_text2]
    fout = open(file_output, "w+")
    for i in range(1,len(cipher_text)+1):
        for plain_text in plain_texts:
            key = findKey(i,plain_text,cipher_text)
            key1 = setKey(key,message)
            print("decryption of message: {} for plaintext: {} and key: {}".format(decrypt(key1,message),plain_text,key))
            fout.write("decryption of message: {} for plaintext: {} and key: {}\n".format(decrypt(key1,message),plain_text,key))
    print("We can clearly understand the key from this")

if __name__ == "__main__":
    main()