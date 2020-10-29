CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

def mod26(num):
    return (num%26)

def getKey(cipherText, plainText):
    return mod26(int(CHARACTERS.upper().find(cipherText[0]) - CHARACTERS.find(plainText[0])))

def main():
    cipherText = "XLILSYWIMWRSAJSVWEPIJSVJSYVQMPPMSRHSPPEVWMXMWASVXLQSVILYVVCFIJSVIXLIWIPPIVVIGIMZIWQSVISJJIVW"  #gt pt
    print(cipherText)
    plainText_corresponding_to_CT = "thehouseisnowforsaleforfourmilliondollarsitisworthmorehurrybeforethesellerreceivesmoreoffers"
    print("KEY : {}".format(getKey(cipherText,plainText_corresponding_to_CT)))

if __name__ == "__main__":
    main()