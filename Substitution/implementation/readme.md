The implementation of the Simple Substitution Cipher (Substitution.py)

Here the given message is both enctypted and decrypted using the key given. The key is actually a string with all characters from "a-z" in a specific order. This is basically the one to one mapping between actual letters and the key to form the cipher text.

Assumptions -- logical assumptions were made following the textbook conventions:
    1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
    2. Input message should be given in the input file as "message = <input message to encrypt and decrypt back>"
    3. key. Input should be given as "key = <key value> "
    4. Output will be of the form "<encrypted message(in CAPS)> \n <decrypted message (input given)>"

Input : ./Substitution/input.txt
Output : ./Substitution/output.txt

*To set the input file path please edit the Substitution.py file -- there is a "file_input" variable that can be set to the file of the required input
*To set the output file path please edit the Substitution.py file -- there is a "file_output" variable that can be set to the file of the required output

*Note : to encrypt and decrypt a message with a pair of specific keys all that needs to be done is run the Substitution.py file. The output will be : The first line Encrypted string and next line Decrypted string.
*Note the key should contain all the characters, i.e, alphabet mapping from a-z in lowercase
*Note: use space characters after and before "=" in input as given in the file
