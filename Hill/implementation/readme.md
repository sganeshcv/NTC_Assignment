The implementation of the Hill Cipher (Hill.py)

The formula used is same as that mentioned in the text book :: C = P.K & P = C.Kinv

Assumptions -- logical assumptions were made following the textbook conventions:
    1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
    2. Input key_dimension should be given in the input file as "key_dimension = <input key_dimension>" --integer
    3. key -> key should be given as a string "key = <input key value as string>" which will be later changed as a matrix in Z26
    4. Input message should be given in the input file as "message = <input message to encrypt and decrypt back>"
    5. Output will be of the form "<encrypted message(in CAPS)> \n <decrypted message (input given)>"

Input : ./Hill/input.txt
Output : ./Hill/output.txt

*To set the input file path please edit the Hill.py file -- there is a "file_input" variable that can be set to the file of the required input
*To set the output file path please edit the Hill.py file -- there is a "file_output" variable that can be set to the file of the required output

*Note : to encrypt and decrypt a message with a key all that needs to be done is run the Hill.py file. The output will be : The first line Encrypted string and next line Decrypted string (given as input).
*Note: use space characters after and before "=" in input as given in the file
*Note: the key should have a matrix inverse in Z26

