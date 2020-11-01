kassiski test:
    attack for vigenere cipher as menioned in the text book is implemented. For the the assumptions as in the text were made. In the case where a monogramic statistical attack wasn't enough a BruteForce method was implemented on top of that to get the final output
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. Input message should be given in the input file as "message = <input message value>" -- lower case string
        3. The output will be a list of possible solutions (since a single monogram statistical attack was not sufficient to decipher a bruteforce method was used)

*Note: use space characters after and before "=" in input as given in the file

knownPT:
    Assumption here is that the adversary knows the key length and a pair of plaintext, corresponding ciphertext. The the adversary can perform this attack to find out the exact key value
        1. Input should contain "plain_text = <value of plain text>"
        2. Input next line should have "cipher_text = <value of corresponding cipher text>"
        3. Input last line is the key length "key_length = <integer value of length of key>"
        4. output will be the key in lower case

chosenPT:
    Assumption here is that the adversary can choose a plain text and will be provided 2 possible cipher text corresponding to the plain text. He will also have another encrypted message which he has to decrypt. The main condition of this attack will be that the key length will be less than or equal to the plain text and minimum key length is 1.
        1. Input message (to decrypt) should be given in the input file as "message = <input message to encrypt and decrypt back>"
        2. Input should contain "plain_text = <value of plain text>"
        3. Input next line should have "cipher_text1 = <value of corresponding cipher text>" and the next one (cipher_text1) in the next sentence similar to cipher_text1
        4. output will be the key in lower case
    There will be a number of possible decryption but the correct one can be identified from the final decrypted values

chosenCT:
    Assumption here is that the adversary can choose a cipher text and will be provided 2 possible plain text corresponding to the cipher text. He will also have another encrypted message which he has to decrypt. The main condition of this attack will be that the key length will be less than or equal to the cipher text and minimum key length is 1.
        1. Input message (to decrypt) should be given in the input file as "message = <input message to encrypt and decrypt back>"
        2. Input should contain "cipher_text = <value of cipher text>"
        3. Input next line should have "plain_text1 = <value of corresponding plain text>" and the next one)(plain_text2) in the next sentence similar to plain_text1
        4. output will be the key in lower case
    There will be a number of possible decryption but the correct one can be identified from the final decrypted values