CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def mod26(num):
    return (num%26)

def getKey(cipherText, plainText):
    return mod26(int(CHARACTERS.upper().find(cipherText[0]) - CHARACTERS.find(plainText[0])))

def main():
    chosen_CipherText = "A"  #gt pt
    print(chosen_CipherText)
    plainText_corresponding_to_CT = "t"  #gt
    print("KEY : {}".format(getKey(chosen_CipherText,plainText_corresponding_to_CT)))

if __name__ == "__main__":
    main()