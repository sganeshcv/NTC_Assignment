file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Shift/cryptanalysis/knownPT/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Shift/cryptanalysis/knownPT/output.txt"

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def mod26(num):
    return (num%26)

def getKey(cipherText, plainText):
    return mod26(int(CHARACTERS.upper().find(cipherText[0]) - CHARACTERS.find(plainText[0])))

def main():
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.find("cipherText") != -1:    
                cipherText = (line.rstrip('\n').split(" = ")[1])
            elif line.find("plainText_corresponding_to_CT") != -1:
                plainText_corresponding_to_CT = (line.rstrip('\n').split(" = ")[1])
    fout = open(file_output, "w+")
    print("KEY : {}".format(getKey(cipherText,plainText_corresponding_to_CT)))
    fout.write("KEY : {}".format(getKey(cipherText,plainText_corresponding_to_CT)))

if __name__ == "__main__":
    main()