import sys
file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Shift/implementation/Shift/B17063CS_Sreeganesh_3_I.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Shift/implementation/Shift/B17063CS_Sreeganesh_3_O.txt"

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def mod26(num):
    return (num%26)


def encrypt(key,message):
    cipherText = ''
    for character in message:
        if character in CHARACTERS:
            character_index = CHARACTERS.find(character)
            cipherText += CHARACTERS[mod26(character_index + key)].upper()
        else:
            cipherText += character
    return cipherText

def decrypt(key,message):
    plainText = ''
    for character in message:
        if character in CHARACTERS.upper():
            character_index = CHARACTERS.upper().find(character)
            plainText += CHARACTERS[mod26(character_index - key)]
        else:
            plainText += character
    return plainText
            

def keyValidation(key):
    if  key < 0:
        sys.exit("The key should be greater than or equal to zero!!")

def main():
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.find("message") != -1:    
                message = (line.rstrip('\n').split(" = ")[1])
            elif line.find("key") != -1:
                key = int(line.rstrip('\n').split(" = ")[1])
    fout = open(file_output, "w+")
    keyValidation(key)
    cipherText = encrypt(key,message)
    print(cipherText)
    fout.write(cipherText)
    fout.write("\n")
    plainText = decrypt(key,cipherText)
    print(plainText)
    fout.write(plainText) 

if __name__ == "__main__":
    main()