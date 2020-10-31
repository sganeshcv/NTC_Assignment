The implementation of the Transposition Cipher (KeyedTransposition.py & KeylessTransposition.py)

The method of encryption for keyless transposition is the matrix method same as listed in the textbook.
For keyed and keyless transaposition extra character required will be added with "z".

Assumptions -- logical assumptions were made following the textbook conventions:
    1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
    2. For both the files a sample input has been attached. The same variables are required and in the same manner without adding any extra characters or any unnecessary whitespaces
    3. Sample outputs have also been added displaying the format

Note for the keyed transposition cipher the key should be given as a array with integers denoting the mapping position (strats from 1 and not zero!!)

Input : ./keyedTransposition/input.txt & ./keylessTransposition/input.txt
Output : ./keyedTransposition/output.txt & ./keylessTransposition/output.txt

*To set the input file path please edit the python file -- there is a "file_input" variable that can be set to the file of the required input
*To set the output file path please edit the python file -- there is a "file_output" variable that can be set to the file of the required output

*Note : to encrypt and decrypt a message with a key all that needs to be done is run the corresponding ".py" file. The output will be : The first line Encrypted string and next line Decrypted string (given as input).
*Note: use space characters after and before "=" in input as given in the file
*Note: the key should have a matrix inverse in Z26

