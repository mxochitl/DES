# DES
Milena Gonzalez
Cryptography4230 

<h1>Testing</h1>
To run my code on your local machine, open 2 separate terminals. Run the server.py file and the client.py file respectively. These will provide a command line interface. The terminal acting as the client will prompt you for input (the initial input doesn't matter). You will be asked to input an 8-bit binary string. The client will then encrypt the text and send it off to the server which will then decrypt it and send it back. The client code will prompt you for more input unless the input is 'q'. All of my implementation of the DES algorithm is in the DES.py file.

<h1>Implementation</h1>
I plan to change the way I store the master key to improve security. If you want to change the initial/master key, you will have to go into both the server and client files and change the string variable labeled key10bit. I use that to get k1 and k2 in each file to use for the encrypt/decrypt function. Both functions call the generateKeys function which takes in a 10bit key, permutates, splits, left shifts, concatenates, and permutates again in various orders to get these 2 distinct keys.

The encryption function takes in the plain text, permutates it and splits it. Half of the permutated string is sent to the F function, which is a whole other beast. The F function takes the 4bits, permutates it twice in different ways, concatenates the two, and xor’s it with the first key. That product is then split again and sent to different s boxes. I have seperate functions for each of the s boxes to account for the different substitution matrices. First split the 4bit input by indices, grouping the first and last and the middle two into seperate variables. To get the desired row and column of the matrix, I had to convert these values to base 2 integers. I used the row and column to find the substitution value, convert it length 2 binary and return it from the s box function. The output of the f function is xor-ed with the first half of the split text. This process is repeated with k2 as an input in the f-function. There is one last permutation and then you have the cipher text! Decryption is pretty much the same code, but the order of using k1 and k2 switch. 

This was the first class I actually want to spend time adding more to my hw than the basic requirements (even after the due date)! I actually really liked learning about and implementing the cryptography algorithm. I am really glad the assignment included the communication between servers because I may have never tried to write that code otherwise. I have always been adamant that I would never go into security (mostly because it sounded hard and is a very niche crowd to say the least), but after this hw I'm thinking about it. I was expecting to drop this class, but I'm glad I tried it out. Looking forward to the rest of the semester:) 


