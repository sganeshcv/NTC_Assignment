All the files related to a particular cipher are its cryptanalysis are inside the respective folders. Each folder also has a readme file that describes the process and the assumptions taken. All the files are written in python. The input and  output files are inside all the respective folders. The file path is written in accordance my file system. Before executing the code change the file_input, file_output variables.

The plain text for input or output is completely in lower case and the cipher text in upper case.

Just like in the text book no special characters are allowed in the input or the output. Not even any whitespaces. 

For any cipher algorithms if required a bogus character has been added to make the plain text match the required key size. For those cryptanalysis also the input mush be including the bogus charatcers. 

Most of the input outputs test cases are based on textbook examples.

Most of the algorithms implemented are also examples from the text book.

Sometimes plain text is abbriviated as PT and cipher text as CT.

Most of the plain text attacks are written in a general case. Some general cases with assumptions for the plain text attacks are mentioned in the readme files of the corresponding cipher's cryptanalysis. For the general case implemented to distingush the wrong CT from the right one we have another messgae that will be decrypted using the keys from the PT, CT1 CT2 set. Similar iss the case for chosen CT. One such general case is the wrong set of characters provided in one of the CT corresponding to the chosen Plain text. That special case is not considered seperately, it comes under the general algorithm for each cipher's cryptananlysis.(Although any such special case the correct CT or PT from the incorrect one can be seperated by just a glance).