CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

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
    message = "HIJKLMNN"  #gt pt
    print(message)
    for key in range(1,26):
        plainText = decrypt(key,message)
        print("{} : {}".format(key, plainText)) 

if __name__ == "__main__":
    main()