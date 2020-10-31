The implementation of the Simple Substitution Cipher Cryptanalysis : "substitution_chosenPT.py"

ChosenPT:
  Implemented this attack based on the most obvious case where we chose a Plain text "ab....z" and the adversary provided with two possible ciphertexts. The Objective of the challenger was to find the Key and Decrypt another plain text. Clearly the most obvious choice for the PT for the challenger is "a...z"
    Input : ./chosenPT/input.txt
    Output : ./chosenPT/output.txt  
  
    Assumptions -- logical assumptions were made following the textbook conventions:
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. Input message (to decrypt) should be given in the input file as "message = <input message to encrypt and decrypt back>"
        3. The chosen Plain text should be given as "chosen_plainText = <input value of chosen PT>"
        4. The cipher texts corresponding to that plaintext should be given as "CipherText_corresponding_to_CT1 = <input value for CipherText_corresponding_to_CT1>" and similarly for CipherText_corresponding_to_CT2, but in the next line
        5. The output will be showing the decryption of the message
        6. The key value is clear from the final output the