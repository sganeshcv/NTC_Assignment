file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Substitution/cryptanalysis/chosenCT/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Substitution/cryptanalysis/chosenCT/output.txt"

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def decrypt(keys,message):
    plainText = ''
    for character in message:
        if character in CHARACTERS.upper(): 
            character_index = keys.upper().find(character)
            plainText += CHARACTERS[character_index]
        else:
            plainText += character
    return plainText

def getKey(plainText,cipherText):
    key = ""
    for char in CHARACTERS:
        key += cipherText.lower()[plainText.find(char)]
    return key

def main(): 
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.find("message") != -1:    
                message = (line.rstrip('\n').split(" = ")[1])
            elif line.find("chosen_cipherText") != -1:
                chosen_cipherText = (line.rstrip('\n').split(" = ")[1])
            elif line.find("PlainText_corresponding_to_CT1") != -1:
                PlainText_corresponding_to_CT1 = (line.rstrip('\n').split(" = ")[1])
            elif line.find("PlainText_corresponding_to_CT2") != -1:
                PlainText_corresponding_to_CT2 = (line.rstrip('\n').split(" = ")[1])
    fout = open(file_output, "w+")
    print("Since the Obvious choice of PT will be a-z, one of the corresponding CTs will be the actual key. To find out all we have to do is solve the message using all the keys and select the one corresponding to a meaning.")
    print(decrypt(getKey(PlainText_corresponding_to_CT1,chosen_cipherText),message))
    print(decrypt(getKey(PlainText_corresponding_to_CT2,chosen_cipherText),message))
    fout.write(decrypt(getKey(PlainText_corresponding_to_CT1,chosen_cipherText),message))
    fout.write("\n")
    fout.write(decrypt(getKey(PlainText_corresponding_to_CT2,chosen_cipherText),message))
    print("We can clearly the key from the decrypted message!!")

if __name__ == "__main__":
    main()