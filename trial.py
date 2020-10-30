file_path = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Affine/cryptanalysis/chosenPT/input.txt"
with open (file_path, 'rt') as myfile:
        for line in myfile:
            if line.lower().find("message") != -1:    # if case-insensitive match,
                message = line.rstrip('\n').split(" = ")[1]
            elif line.find("chosen_plainText") != -1:
                chosen_plainText = line.rstrip('\n').split(" = ")[1]
            elif line.find("CipherText_corresponding_to_CT1") != -1:
                CipherText_corresponding_to_CT1 = line.rstrip('\n').split(" = ")[1]
            elif line.find("CipherText_corresponding_to_CT2") != -1:
                CipherText_corresponding_to_CT2 = line.rstrip('\n').split(" = ")[1]

print(message)
print(chosen_plainText)
print((CipherText_corresponding_to_CT1))
print(CipherText_corresponding_to_CT2)