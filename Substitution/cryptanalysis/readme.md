The implementation of the Simple Substitution Cipher Cryptanalysis : "substitution_chosenPT.py"

Note: Implementing a Bruteforce here is extremly ineficient!!

ChosenPT:
  Implemented this attack based on the most obvious case where we chose a Plain text "ab....z" and the adversary provided with two possible ciphertexts. The Objective of the challenger was to find the Key and Decrypt another plain text. Clearly the most obvious choice for the PT for the challenger is "a...z"
    Input : ./chosenPT/input.txt
    Output : ./chosenPT/output.txt  
  
    Assumptions -- logical assumptions were made following the textbook conventions:
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. Input message (to decrypt) should be given in the input file as "message = <input message to encrypt and decrypt back>"
        3. The chosen Plain text should be given as "chosen_plainText = <input value of chosen PT>"
        4. The cipher texts corresponding to that plaintext should be given as "CipherText_corresponding_to_CT1 = <input value for CipherText_corresponding_to_CT1>" and similarly for CipherText_corresponding_to_CT2, but in the next line
        5. The output will be showing the possible decryptions of the message
        6. The key value will be clear from the final output 

  **In a special case one of the CT wont be having all the characters in that case the correct CT is obviously the other one with all characters from a-z. Another special case is same as that of the special case of shift chosenPT attack. Plain text will be 2 same characters but one of the cipher text wont contain the same characters. The other one is therefore the answer.

ChosenCT:
  Implemented this attack based on the most obvious case again where we chose a cipher text "ab....z" and the adversary provided with two possible plain texts. The Objective of the challenger was to find the Key and Decrypt another message. Clearly the most obvious choice for the CT for the challenger is "a...z"
    Input : ./chosenCT/input.txt
    Output : ./chosenCT/output.txt  
  
    Assumptions -- logical assumptions were made following the textbook conventions:
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. Input message (to decrypt) should be given in the input file as "message = <input message to encrypt and decrypt back>"
        3. The chosen Cipher text should be given as "chosen_cipherText = <input value of chosen CT>"
        4. The plain texts corresponding to that cipher text should be given as "PlainText_corresponding_to_CT1 = <input value for PlainText_corresponding_to_CT1>" and similarly for PlainText_corresponding_to_CT1, but in the next line
        5. The output will be showing the possible decryptions of the message
        6. The key value will be clear from the final output the

  **The special cases is also applicable here but instead the other way around (instead of the cipher text it'll be the plain text and vice versa). 

KnownPT:
  Like any other known plaintext attacks here also the adversary is provided with a plain text cipher text pair. The objective is to find the key
    Input : ./chosenCT/input.txt
    Output : ./chosenCT/output.txt  

    Assumptions -- logical assumptions were made following the textbook conventions:
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. The Plain text should be given as "plainText = <input value of PT>"
        3. The cipher text corresponding to that plaintext should be given as "cipherText = <input value for CT>" 
        4. The output will be showing the key used for enctypion