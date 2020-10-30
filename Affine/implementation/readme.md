The implementation of the Affine Cipher (Affine.py)

Assumptions -- logical assumptions were made following the textbook conventions:
    1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
    2. Input message should be given in the input file as "message = <input message to encrypt and decrypt back>"
    3. key1 -> multiplication key; key2 -> addition key. Input should be given as "key1 = <key1 value> " next line "key2 = <key2 value>"
    4. Output will be of the form "<encrypted message(in CAPS)> \n <decrypted message (input given)>"

Input : ./Affine/input.txt
Output : ./Affine/output.txt

*To set the input file path please edit the Affine.py file -- there is a "file_input" variable that can be set to the file of the required input
*To set the output file path please edit the Affine.py file -- there is a "file_output" variable that can be set to the file of the required output

*Note : to encrypt and decrypt a message with a pair of specific keys all that needs to be done is run the Affine.py file. The output will be : The first line Encrypted string and next line Decrypted string.
*Note: use space characters after and before "=" in input as given in the file
