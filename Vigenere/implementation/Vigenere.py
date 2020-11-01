import sys

file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Vigenere/implementation/Vigenere/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Vigenere/implementation/Vigenere/output.txt"

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def mod26(num):
    return (num%26)

def setKey(key,message):
    while len(key) < len(message):
        key += key
    return key

def encrypt(keys,message):
    cipherText = ''
    for (character,i) in zip(message,range(0,len(message))):
        if character in CHARACTERS:
            character_index = CHARACTERS.find(character)
            key_indeex = CHARACTERS.find(keys[i])
            cipherText += CHARACTERS[mod26(character_index + key_indeex)].upper()
        else:
            cipherText += character
    return cipherText

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
            

def keyValidation(keys):
    for key in keys:
        if  key not in CHARACTERS:
            sys.exit("The key should be greater than or equal to zero!!")

def main():
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.find("message") != -1:    
                message = (line.rstrip('\n').split(" = ")[1])
            elif line.find("key") != -1:
                key0 = (line.rstrip('\n').split(" = ")[1])
    
    fout = open(file_output, "w+")
    keyValidation(key0)
    key = setKey(key0,message)
    cipherText = encrypt(key,message)
    print(cipherText)
    fout.write(cipherText+ "\n")
    plainText = decrypt(key,cipherText)
    fout.write(plainText)
    print(plainText) 

if __name__ == "__main__":
    main()