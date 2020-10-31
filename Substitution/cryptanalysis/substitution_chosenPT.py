file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Substitution/cryptanalysis/chosenPT/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Substitution/cryptanalysis/chosenPT/output.txt"

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

def main(): 
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.find("message") != -1:    
                message = (line.rstrip('\n').split(" = ")[1])
            elif line.find("chosen_plainText") != -1:
                chosen_plainText = (line.rstrip('\n').split(" = ")[1])
            elif line.find("CipherText_corresponding_to_CT1") != -1:
                CipherText_corresponding_to_CT1 = (line.rstrip('\n').split(" = ")[1])
            elif line.find("CipherText_corresponding_to_CT2") != -1:
                CipherText_corresponding_to_CT2 = (line.rstrip('\n').split(" = ")[1])
    fout = open(file_output, "w+")

    print("Since the Obvious choice of PT will be a-z, one of the corresponding CTs will be the actual key. To find out all we have to do is solve the message using all the keys and select the one corresponding to a meaning.")
    print(decrypt(CipherText_corresponding_to_CT1,message))
    print(decrypt(CipherText_corresponding_to_CT2,message))
    fout.write(decrypt(CipherText_corresponding_to_CT1,message))
    fout.write("\n")
    fout.write(decrypt(CipherText_corresponding_to_CT2,message))
    print("We can clearly the key from the decrypted message!!")

if __name__ == "__main__":
    main()