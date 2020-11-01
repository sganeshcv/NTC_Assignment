file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Substitution/cryptanalysis/knownPT/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Substitution/cryptanalysis/knownPT/output.txt"

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def getKey(plainText,cipherText):
    key = ""
    for char in CHARACTERS:
        key += cipherText.lower()[plainText.find(char)]
    return key

def main(): 
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.find("plainText") != -1:    
                plainText = (line.rstrip('\n').split(" = ")[1])
            elif line.find("cipherText") != -1:
                cipherText = (line.rstrip('\n').split(" = ")[1])
            
            
    fout = open(file_output, "w+")

    print("Key:")
    print(getKey(plainText,cipherText))
    fout.write(getKey(plainText,cipherText))
    fout.write("\n")

if __name__ == "__main__":
    main()