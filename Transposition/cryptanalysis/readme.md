The implementation of the Shift Cipher Cryptanalysis : shift_bruteforce.py , shift_chosenCT.py, shift_chosenPT.py, shift_knownPT.py & shift_statistical.py

Note: The plaintext and cipher texts provided as inputs for the cryptanalysis must contain the bogus character if it was necessary for encryption in the first place.

Bruteforce (keyless Transposition):
  The implementation of this attack was done by considering only the possible split values for a given cipher text. That is if a cipher text has a size n, then the list of possible split size are not 1 to n, where as it is just the factors of n.  F
    Input : ./bruteforce/input.txt
    Output : ./bruteforce/output.txt  
  
    Assumptions -- logical assumptions were made following the textbook conventions:
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. Input cipher text (to find the plain text) should be given in the input file as "cipherText = <input value>" -- Uppercase
        3. The output will be showing all the possible decryption of the CT

Note: BruteForce on keyed Transposition is inefficient

knownPT (keyed Transposition):
  Similar to the Plain Text attack for Hill cipher given in textbook this was also implemented accordingly. The challenger will have a pair of Plain text and the corresponding cipher text. Now he/she has to figure out the keys from this and decrypt another message.
    Input : ./knownPT/input.txt
    Output : ./knownPT/output.txt  
    
    Assumptions --
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. A message to decrypt after finding the keys should be given as "message = <value of message>" -- no special characters
        3. The known plainText should be given as "plainText = <input value of plain Text chosen>" -- lower case only
        4. The cipherText corresponding to that cipher text corresponding to plain text should be given as "cipherText = <input value for the cipher text>"
        5. The output will be showing the Key used in that pair

chosenPT (keyed Transposition):
  Here the adversary will be given 2 cipher texts corresponding to a plain text he/she chooses. One of which is correct. The adversary has to find out the key and decrypt another message using the key. The adversary after trying the possibilities will find out the right key based on the decryption. Assumption : The plain text cipher texts are valid pairs. 
    Input : ./chosenPT/input.txt
    Output : ./chosenPT/output.txt  
    
    Assumptions --
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. A message to decrypt after finding the keys should be given as "message = <value of message>" -- no special characters
        3. The known plainText should be given as "plainText = <input value of plain Text chosen>" -- lower case only
        4. The cipherText corresponding to that plain text should be given as "cipherText1 = <input value for the cipher text>" simialrly for cipherText2 in the next line. -- upper case
        5. The output will be showing the Key and the decryption corresponding to that.

        After decrypting the final message the adversary will be able to clearly see the actual key used.

chosenCT (keyed Transposition):
  Here the adversary will be given 2 plain texts corresponding to a cipher text he/she chooses. One of which is correct. The adversary has to find out the key and decrypt another message using the key. The adversary after trying the possibilities will find out the right key based on the decryption. Assumption : The plain text cipher texts are valid pairs. 
    Input : ./chosenCT/input.txt
    Output : ./chosenCT/output.txt  
    
    Assumptions --
        1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
        2. A message to decrypt after finding the keys should be given as "message = <value of message>" -- no special characters
        3. The known cipherText should be given as "cipherText = <input value of cipher Text chosen>" -- upper case only
        4. The plain text corresponding to that cipher text should be given as "plainText1 = <input value for the plain text>" simialrly for plainText2 in the next line. -- lower case
        5. The output will be showing the Key and the decryption corresponding to that.

        After decrypting the final message the adversary will be able to clearly see the actual key used.

*Note: use space characters after and before "=" in input as given in the file
*Note: the input should be a valid PT and it's corresponding CT for the alogorithm to work


*To set the input file path please edit the corresponding python file -- there is a "file_input" variable that can be set to the file of the required input
*To set the output file path please edit the corresponding python file -- there is a "file_output" variable that can be set to the file of the required output


*Note: use space characters after and before "=" in input as given in the current input file
