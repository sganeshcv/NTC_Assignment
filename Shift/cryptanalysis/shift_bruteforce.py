CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Shift/cryptanalysis/bruteForce/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Shift/cryptanalysis/bruteForce/output.txt"

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

def main():
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.find("message") != -1:    
                message = (line.rstrip('\n').split(" = ")[1])
    fout = open(file_output, "w+")
    print(message)
    for key in range(1,26):
        plainText = decrypt(key,message)
        print("{} : {}".format(key, plainText)) 
        fout.write("{} : {}\n".format(key, plainText))

if __name__ == "__main__":
    main()