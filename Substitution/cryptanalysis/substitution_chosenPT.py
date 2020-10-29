CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def decrypt(keys,message):
    plainText = ''
    for character in message:
        if character in CHARACTERS.upper(): 
            character_index = keys.upper().find(character)
            plainText += CHARACTERS[character_index]
        else:
            plainText += character
    return plainText

def main():
    message = "ICFVQRVVNEFVRNVSIYRGAHSLIOJICNHTIYBFGTICRXRS"
    chosen_plainText = "abcdefghijklmopqrstuvwxyz"  #this is the most obvious choice
    CipherText_corresponding_to_CT1 = "KXVMCNOPHQRSZYIJADLEGWBUFT"  #gt ct in caps
    CipherText_corresponding_to_CT2 = "NOATRBECFUXDQGYLKHVIJMPZSW"  #gt ct in caps
    CipherText_corresponding_to_CT3 = "LXSFCZJKNVBPYWGTEOIHMAURQD"  #get ct in caps    
    print("Since the Obvious choice of PT will be a-z, one of the corresponding CTs will be the actual key. To find out all we have to do is solve the message using all the keys and select the one corresponding to a meaning.")
    print(decrypt(CipherText_corresponding_to_CT1,message))
    print(decrypt(CipherText_corresponding_to_CT2,message))
    print(decrypt(CipherText_corresponding_to_CT3,message))
    print("We can clearly the key from the decrypted message!!")

if __name__ == "__main__":
    main()