A knownPT attack for HILL cipher as menioned in the text book is implemented. For the the assumptions as in the text were made. That is the key matrix dimension and a pair of plain text as well as the corresponding cipher text is also needed for the challenger. 

    1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
    2. Input key dimension should be given in the input file as "key_dimension = <input key dimension value>"
    3. The known Plain tesxt should be given as "known PT = <input value of chosen PT>"
    4. The cipher texts corresponding to that plaintext should be given as "cipherText = <input value for the corresponding cipher text>" in caps 
    5. The output will be showing the Key matrix in Z26

The chosen plaintext attack is done on a chosen plain text by the adversary who receives more than one CT corresponding to that. Here the assumption is that the adversary knows the key dimensions. And the code will raise an error on the case where the inverse doesn't exist for the input case. In that case the input can be tested by reversing the cipher text order.

    1. All the input should be given without including any of the special characters or new lines or even whitespace. The input must be given all in small letters. 
    2. A message to decrypt after finding the keys should be given as "message = <value of message>" -- no special character all upper case
    3. Input key dimension should be given in the input file as "key_dimension = <input key dimension value>" - integer
    3. The known Plain tesxt should be given as "known PT = <input value of chosen PT>"
    4. The cipher texts corresponding to that plaintext should be given as "cipherText1 = <input value for the corresponding cipher text>" and same for ciphertext2 in caps 
    5. The output will be showing the Key matrix in Z26 and corresponding decryption. The oput will contain a 

    If both the CTs are valid cases the message will also be decrypted.

*Note: use space characters after and before "=" in input as given in the file
*Note: the input should be a valid PT and it's corresponding CT for the alogorithm to work