The implementation of the Vigenere Cipher (Vigenere.py)

The input used was the same as listed in the textbook.

Assumptions -- logical assumptions were made following the textbook conventions:
    1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
    2. Input message should be given in the input file as "message = <input message>" --lower case string
    3. key -> key should be given as a string "key = <input key value as string>" which will be repeated to make it reach the input message length
    4. Output will be of the form "<encrypted message(in CAPS)> \n <decrypted message (input given in lower case)>"

Input : ./Vigenere/input.txt
Output : ./Vigenere/output.txt

*To set the input file path please edit the Vigenere.py file -- there is a "file_input" variable that can be set to the file of the required input
*To set the output file path please edit the Vigenere.py file -- there is a "file_output" variable that can be set to the file of the required output

*Note : to encrypt and decrypt a message with a key all that needs to be done is run the Vigenere.py file. The output will be : The first line Encrypted string and next line Decrypted string (given as input).
*Note: use space characters after and before "=" in input as given in the file