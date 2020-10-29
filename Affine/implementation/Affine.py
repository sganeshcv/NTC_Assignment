import sys

CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
KEYDOMAIN = [ 1,  3,  5,  7,  9,  11,  15,  17,  19,  21,  23,  25 ]  #key domain for key1

def mod(num):
    m = len(CHARACTERS)
    return (num%m)

def modInverse(num): 
    m = len(CHARACTERS)
    num = num % m
    for x in range(1, m) : 
        if ((num * x) % m == 1): 
            return x 
    return 1

def encrypt(keys,message):
    cipherText = ''
    for character in message:
        if character in CHARACTERS:
            character_index = CHARACTERS.find(character)
            cipherText += CHARACTERS[mod(character_index * keys[0] + keys[1])].upper()
        else:
            cipherText += character
    return cipherText

def decrypt(keys,message):
    plainText = ''
    for character in message:
        if character in CHARACTERS.upper():
            character_index = CHARACTERS.upper().find(character)
            plainText += CHARACTERS[mod((character_index - keys[1]) * modInverse(keys[0]))]
        else:
            plainText += character
    return plainText
            

def keyValidation(key1, key2):
    if key1 not in KEYDOMAIN:
        sys.exit("The first key value is not in the kwy domain")
    elif key2 < 0:
        sys.exit("The second key should be greater than or equal to zero!!")

def main():
    message = "ahgd"  #gt pt
    key1 = 7         #gt keys
    key2 = 0
    keys = [key1, key2]
    keyValidation(keys[0],keys[1])
    cipherText = encrypt(keys,message)
    print(cipherText)
    plainText = decrypt(keys,cipherText)
    print(plainText)    

if __name__=="__main__":
    main()
