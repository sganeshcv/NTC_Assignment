CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Shift/cryptanalysis/chosenCT/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Shift/cryptanalysis/chosenCT/output.txt"

def mod26(num):
    return (num%26)

def decrypt(key,message):
    plainText = ''
    for character in message:
        if character in CHARACTERS.upper():
            character_index = CHARACTERS.upper().find(character)
            plainText += CHARACTERS[mod26(character_index - key)]
        else:
            plainText += character
    return plainText

def getKey(cipherText, plainText):
    return mod26(int(CHARACTERS.upper().find(cipherText[0]) - CHARACTERS.find(plainText[0])))

def main():
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.lower().find("message") != -1:    # if case-insensitive match,
                message = line.rstrip('\n').split(" = ")[1]
            elif line.find("chosen_CipherText") != -1:
                chosen_CipherText = line.rstrip('\n').split(" = ")[1]
            elif line.find("plainText1_corresponding_to_CT") != -1:
                plainText1_corresponding_to_CT = line.rstrip('\n').split(" = ")[1]
            elif line.find("plainText2_corresponding_to_CT") != -1:
                plainText2_corresponding_to_CT = line.rstrip('\n').split(" = ")[1]
    
    fout = open(file_output, "w+")

    print("KEY : {} Decrypted Message : {}\n".format(getKey(chosen_CipherText,plainText1_corresponding_to_CT), decrypt(getKey(chosen_CipherText,plainText1_corresponding_to_CT),message)))
    print("KEY : {} Decrypted Message : {}\n".format(getKey(chosen_CipherText,plainText2_corresponding_to_CT), decrypt(getKey(chosen_CipherText,plainText2_corresponding_to_CT),message)))

    fout.write("KEY : {} Decrypted Message : {}\n".format(getKey(chosen_CipherText,plainText1_corresponding_to_CT), decrypt(getKey(chosen_CipherText,plainText1_corresponding_to_CT),message)))
    fout.write("KEY : {} Decrypted Message : {}\n".format(getKey(chosen_CipherText,plainText2_corresponding_to_CT), decrypt(getKey(chosen_CipherText,plainText2_corresponding_to_CT),message)))

if __name__ == "__main__":
    main()