import sys

file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Substitution/implementation/Substitution/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Substitution/implementation/Substitution/output.txt"

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def keyValidation(key):
    if  key not in CHARACTERS:
        sys.exit("The key should be greater than or equal to zero!!")

def encrypt(keys,message):
    cipherText = ''
    for character in message :
        if character in CHARACTERS:
            character_index = CHARACTERS.find(character)
            cipherText += keys[character_index].upper()
        else:
            cipherText += character
    return cipherText

def decrypt(keys,message):
    plainText = ''
    for character in message:
        if character in CHARACTERS.upper(): 
            character_index = keys.upper().find(character)
            plainText += CHARACTERS[character_index]
        else:
            plainText += character
    return plainText

def main():
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.find("message") != -1:    
                message = (line.rstrip('\n').split(" = ")[1])
            elif line.find("key") != -1:
                key = (line.rstrip('\n').split(" = ")[1])
            
    fout = open(file_output, "w+")
    cipherText = encrypt(key,message)
    print(cipherText)
    fout.write(cipherText)
    plainText = decrypt(key,cipherText)
    print(plainText) 
    fout.write("\n")
    fout.write(plainText)

if __name__ == "__main__":
    main()