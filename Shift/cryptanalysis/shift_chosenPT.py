CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Shift/cryptanalysis/chosenPT/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Shift/cryptanalysis/chosenPT/output.txt"

def mod26(num):
    return (num%26)

def getKey(cipherText, plainText):
    return mod26(int(CHARACTERS.upper().find(cipherText[0]) - CHARACTERS.find(plainText[0])))


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
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.lower().find("message") != -1:    # if case-insensitive match,
                message = line.rstrip('\n').split(" = ")[1]
            elif line.find("chosen_plainText") != -1:
                chosen_plainText = line.rstrip('\n').split(" = ")[1]
            elif line.find("CipherText_corresponding_to_CT1") != -1:
                CipherText_corresponding_to_CT1 = line.rstrip('\n').split(" = ")[1]
            elif line.find("CipherText_corresponding_to_CT2") != -1:
                CipherText_corresponding_to_CT2 = line.rstrip('\n').split(" = ")[1]
      
    fout = open(file_output, "w+")

    key1 = getKey(CipherText_corresponding_to_CT1,chosen_plainText)
    key2 = getKey(CipherText_corresponding_to_CT2,chosen_plainText)
    print("KEY1 : {}".format(key1))
    print("KEY2 : {}".format(key2))
    print("Now all we have to do is decrypt any large CT using both the keys to find the correct one")
    print("Decryption using KEY : {} => {}".format(key1,decrypt(key1,message)))
    print("Decryption using KEY : {} => {}".format(key2,decrypt(key2,message)))
    fout.write("Decryption using KEY : {} => {}\n".format(key1,decrypt(key1,message)))
    fout.write("Decryption using KEY : {} => {}".format(key2,decrypt(key2,message)))
    print("We can now clearly see the key used for encipherment")



if __name__ == "__main__":
    main()