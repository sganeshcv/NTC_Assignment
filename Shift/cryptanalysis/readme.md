The implementation of the Shift Cipher Cryptanalysis : shift_bruteforce.py , shift_chosenCT.py, shift_chosenPT.py, shift_knownPT.py & shift_statistical.py

Bruteforce:
  The implementation of this attack was done is the most general way. For a given input message/ciphertext (all in uppercase) we try to decrypt it using all the possible 26 keys. In the output the key used for decryption and the decrypted message will be displayed
    Input : ./bruteforce/input.txt
    Output : ./bruteforce/output.txt  
  
    Assumptions -- logical assumptions were made following the textbook conventions:
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. Input message (to decrypt) should be given in the input file as "message = <input message to encrypt and decrypt back>" -- Uppercase
        3. The output will be showing both the keys and the decryption of the message forr all the 26 keys
    
Statistical:
  Implemented this attack with the help of a frequency dictionary text file found online. That was used as a reference for the english frequency characters.
    Input : ./statistical/input.txt
    Output : ./statistical/output.txt  
  
    Assumptions -- logical assumptions were made following the textbook conventions:
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. Input message (to decrypt) should be given in the input file as "message = <input message to encrypt and decrypt back>"
        3. The output will be showing 3 decrypted message decrypted using the most 3 frequent charactes for the message. The three characters used for decryption will also be shown in the output

knownPT:
  Similar to the Plain Text attack for Hill cipher given in textbook this was also implemented accordingly. The challenger will have a pair of Plain text and the corresponding cipher text. Now he/she has to figure out the keys from this.
    Input : ./knownPT/input.txt
    Output : ./knownPT/output.txt  
    
    Assumptions --
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        3. The known cipherText should be given as "cipherText = <input value of cipher Text corresponding to chosen PT>" -- Upper case only
        4. The plainText_corresponding_to_CT corresponding to that cipher text should be given as "plainText_corresponding_to_CT = <input value for the plain text>"
        5. The output will be showing the Key used in that pair

ChosenPT:
  Implemented this attack based on the textbook example of chosen plain text attack on Affine Cipher. Here challenger chooses a Plain text of size one and the adversary provided with two possible ciphertexts. The Objective of the challenger was to find the Key and Decrypt another plain text.
    Input : ./chosenPT/input.txt
    Output : ./chosenPT/output.txt  
  
    Assumptions -- logical assumptions were made following the textbook conventions:
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. Input message (to decrypt) should be given in the input file as "message = <input message to encrypt and decrypt back>"
        3. The chosen Plain tesxt should be given as "chosen_plainText = <input value of chosen PT>"
        4. The cipher texts corresponding to that plaintext should be given as "CipherText_corresponding_to_CT1 = <input value for CipherText_corresponding_to_CT1>" and similarly for CipherText_corresponding_to_CT2, but in the next line
        5. The output will be showing both the keys and the decryption of the message

ChosenCT:
    This is similar to the chosen Plain text attack except here the challenger choses a cipher text insead of a plain text and is provided with some possible plain text. (S)he has to figure out the key and therefore encrypt the additional message provided. 
     Input : ./chosenPT/input.txt
     Output : ./chosenPT/output.txt  
        Assumptions -- logical assumptions were made following the textbook conventions:
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. Input message (to decrypt) should be given in the input file as "message = <input message to encrypt and decrypt back>"
        3. The chosen cipher text should be given as "chosen_CipherText = <input value of chosen CT>"
        4. The plain texts corresponding to that cipher text should be given as "plainText1_corresponding_to_CT = <input value for plainText1 corresponding to CT>" and similarly for plainText2_corresponding_to_CT, but in the next line
        5. The output will be showing both the keys and the decryption of the message


*Note: use space characters after and before "=" in input as given in the file
*Note: the input should be a valid PT and it's corresponding CT for the alogorithm to work


*To set the input file path please edit the corresponding python file -- there is a "file_input" variable that can be set to the file of the required input
*To set the output file path please edit the corresponding python file -- there is a "file_output" variable that can be set to the file of the required output


*Note: use space characters after and before "=" in input as given in the current input file
