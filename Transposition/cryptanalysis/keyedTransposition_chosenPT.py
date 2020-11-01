file_input = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Transposition/cryptanalysis/chosenPT/input.txt"
file_output = "/media/sreeganesh/Windows/Users/GMachine/Documents/Studies/S7/NTC/NTC_Assignment/Transposition/cryptanalysis/chosenPT/output.txt"

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def getfactors(n):
    factors = []
    i = 1
    while i <= n : 
        if (n % i==0) : 
            factors.append(i)
        i += 1
    return factors

def uniqueCharacters(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)): 
            if(str[i] == str[j]):
                return False
    return True
 

def checkfactorValidation(factor, plainText, cipherText):
    for i in range(factor):
        if plainText[i] not in cipherText[0:factor] or cipherText[i] not in plainText[0:factor]:
            return False
    return True

def getUniquePart(key_length, message1):
    i = 0
    while(i+key_length < (len(message1))):
        if(uniqueCharacters(str(message1[i:i+key_length]))):
            return i
        i += key_length
    return -1

def splitGetKey(key_length, plainText, cipherText):
    relative_key = []
    j = getUniquePart(key_length, plainText)
    if(j == -1) or not checkfactorValidation(key_length,plainText[j:j+key_length],cipherText[j:j+key_length]):
        return -1
    for i in range(key_length):
        relative_key.append(plainText[j:j+key_length].find(cipherText[j+i])+1)
    return relative_key

def deshuffle(part_message,key):
    new_message = ""
    for i in range(len(key)):
        index_char = key.index(i+1)
        new_message += part_message[index_char]
    return new_message

def decrypt(keys,message):
    plainText = ''
    i = 0
    while i < len(message):
            plainText += deshuffle(message[i:i+len(keys)],keys)
            i += len(keys)
    return plainText

def main():
    with open (file_input, 'rt') as myfile:
        for line in myfile:
            if line.find("message") != -1:    
                message = (line.rstrip('\n').split(" = ")[1])
            elif line.find("plainText") != -1:
                plainText = (line.rstrip('\n').split(" = ")[1])
            elif line.find("cipherText1") != -1:
                cipherText1 = (line.rstrip('\n').split(" = ")[1]).lower()
            elif line.find("cipherText2") != -1:
                cipherText2 = (line.rstrip('\n').split(" = ")[1]).lower()
    
    fout = open(file_output, "w+")
    factors = getfactors(len(message)) 
    cipherTexts = [cipherText1, cipherText2]   
    for factor in factors:
        if factor != 1:
            for cipherText in cipherTexts:
                if checkfactorValidation(factor,plainText,cipherText):
                    key = splitGetKey(factor,plainText,cipherText)
                    if(key == -1):
                        continue
                    print(key)
                    fout.write(str(key))
                    fout.write(": ")
                    print(decrypt(key,message))
                    fout.write(decrypt(key,message)+"\n")
    print("Now we can clearly see the correct key")

if __name__ == "__main__":
    main()