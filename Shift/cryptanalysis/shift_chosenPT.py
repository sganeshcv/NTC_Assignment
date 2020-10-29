CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

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
    chosen_plainText = "a"  #gt pt
    CipherText_corresponding_to_CT1 = "B"  #gt ct in caps
    CipherText_corresponding_to_CT2 = "E"  #gt ct in caps
    key1 = getKey(CipherText_corresponding_to_CT1,chosen_plainText)
    key2 = getKey(CipherText_corresponding_to_CT2,chosen_plainText)
    print("KEY1 : {}".format(key1))
    print("KEY2 : {}".format(key2))
    print("Now all we have to do is decrypt any large CT using both the keys to find the correct one")
    message = "XLILSYWIMWRSAJSVWEPIJSVJSYVQMPPMSRHSPPEVWMXMWASVXLQSVILYVVCFIJSVIXLIWIPPIVVIGIMZIWQSVISJJIVW"
    print("Decryption using KEY : {} => {}".format(key1,decrypt(key1,message)))
    print("Decryption using KEY : {} => {}".format(key2,decrypt(key2,message)))
    print("We can now clearly see the key used for encipherment")



if __name__ == "__main__":
    main()