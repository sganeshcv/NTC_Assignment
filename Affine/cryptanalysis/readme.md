The implementation of the Affine Cipher Cryptanalysis : "affine_chosePT.py" & "affine_statistical.py"

ChosenPT:
  Implemented this attack based on the textbook example where we chose a Plain text of size two and the adversary provided with two possible ciphertexts. The Objective of the challenger was to find the Key and Decrypt another plain text.
    Input : ./chosenPT/input.txt
    Output : ./chosenPT/output.txt  
  
    Assumptions -- logical assumptions were made following the textbook conventions:
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. Input message (to decrypt) should be given in the input file as "message = <input message to decrypt back>"
        3. The chosen Plain text should be given as "chosen_plainText = <input value of chosen PT>"
        4. The cipher texts corresponding to that plaintext should be given as "CipherText_corresponding_to_CT1 = <input value for CipherText_corresponding_to_CT1>" and similarly for CipherText_corresponding_to_CT2, but in the next line
        5. The output will be showing both the keys and the decryption of the message

knownPT:
  Implemented this attack based on the textbook example where we chose a Plain text of size two and the adversary provided with its ciphertext. The Objective of the challenger was to find the Key.
    Input : ./knownPT/input.txt
    Output : ./knownPT/output.txt  
  
    Assumptions -- logical assumptions were made following the textbook conventions:
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. The chosen Plain text should be given as "chosen_plainText = <input value of chosen PT>"
        3. The cipher texts corresponding to that plaintext should be given as "CipherText_corresponding_to_CT1 = <input value for CipherText_corresponding_to_CT1>" 
        4. The output will be showing both the key pair

ChosenCT:
  Implemented this attack where we chose a cipher text of size two (only 2 possible keys therefore this is sufficient) and the adversary provided with two possible ciphertexts. The Objective of the challenger was to find the Key.
    Input : ./ChosenCT/input.txt
    Output : ./ChosenCT/output.txt  
  
    Assumptions -- logical assumptions were made following the textbook conventions:
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. Input message (to decrypt) should be given in the input file as "message = <input message to decrypt back>"
        3. The chosen cipher text should be given as "chosen_plainText = <input value of chosen PT>" -- uppercase string
        4. The plain texts corresponding to that CT should be given as "PlainText_corresponding_to_CT1 = <input value for PlainText_corresponding_to_CT1>" and similarly for PlainText_corresponding_to_CT2, but in the next line
        5. The output will be showing both the keys

Statistical:
  Implemented this attack with the help of a frequency dictionary text file found online. That was used as a reference for the english frequency characters.
    Input : ./statistical/input.txt
    Output : ./statistical/output.txt  
  
    Assumptions -- logical assumptions were made following the textbook conventions:
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. Input message (to decrypt) should be given in the input file as "message = <input message to encrypt and decrypt back>"
        3. The output will be showing the final decrypted message 


*To set the input file path please edit the corresponding python file -- there is a "file_input" variable that can be set to the file of the required input
*To set the output file path please edit the corresponding python file -- there is a "file_output" variable that can be set to the file of the required output


*Note: use space characters after and before "=" in input as given in the current input file
