All the files related to a particular cipher are its cryptanalysis are inside the respective folders. Each folder also has a readme file that describes the process and the assumptions taken. 

All the files are written in python. The input and  output files are inside all the respective folders. The file path is written in accordance my file system. Before executing the code change the file_input, file_output variables.

The plain text for input or output is completely in lower case and the cipher text in upper case.

Just like in the text book no special characters are allowed in the input or the output. Not even any whitespaces. 

For any cipher algorithms if required a bogus character has been added to make the plain text match the required key size. For those cryptanalysis also the input mush be including the bogus charatcers. 

Most of the input outputs test cases are based on textbook examples.

Most of the algorithms implemented are also examples from the text book.

Sometimes plain text is abbriviated as PT and cipher text as CT.

In some ambigious cases the naming convention has been changed to an obvious one so we can easy distinguish the files. (example B170763CS_Sreeganesh_5_KeyedTransposition.py, B170763CS_Sreeganesh_5_KeylessTransposition.py, etc) 

All the screenshots where the codes are tested with a general input from the text or a common one are attached in the screenshot folder. The screenshot of implementation is named according to the question number (example : B170763CS_Sreeganesh_6.png -- vigenere cipher). All the following are the screenshots of the cryptanalysis techniques used (example B170763CS_Sreeganesh_6.1.png). Each screeshot is taken at the time of that file execution so it has command python filename.py , so we can identify which screeshot refers to which file!! 

Most of the plain text attacks are written in a general case. Some general cases with assumptions for the plain text attacks are mentioned in the readme files of the corresponding cipher's cryptanalysis. For the general case implemented to distingush the wrong CT from the right one we have another messgae that will be decrypted using the keys from the PT, CT1 CT2 set. Similar iss the case for chosen CT. One such general case is the wrong set of characters provided in one of the CT corresponding to the chosen Plain text. That special case is not considered seperately, it comes under the general algorithm for each cipher's cryptananlysis.(Although any such special case the correct CT or PT from the incorrect one can be seperated by just a glance).