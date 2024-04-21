# DataSecurity
Polybius Square Cipher and Myszkowski Transposition Project

Interaction professor [Arbena Musa](https://github.com/ArbenaMusa)

# Language
Project Polybius is developed in Java language and Myszkowski in Python language.

 # HOW TO EXECUTE THE PROGRAM
 
1. Polybius Square Cipher
   
Encryption:
   - Run the program
   - Type E to encrypt
   - Write the key with 5 characters
   - Enter the plaintext
   - See the encrypted text

Decryption:
   - Run the program
   - Type D to decrypt
   - Write the key with 5 characters
   - Enter the ciphertext
   - See the plaintext

2. Myszkowski Transposition Cipher

Encryption:
   - Type 1 to encrypt
   - Enter the plaintext
   - Enter the key (a word)
   - See the encrypted text

Decryption:
   - Type 2 to decrypt
   - Enter the ciphertext
   - Enter the key (a word)
   - See the decrypted text

# DESCRIPTION OF ALGORITHMS

Polybius Square Cipher is a substitution cipher that replaces pairs of letters with coordinates in a grid. The grid typically consists of 5 rows and 5 columns, with letters of the alphabet (usually excluding "J") written inside, each identified by their coordinates. To encode a message, each letter of the plaintext is substituted with a pair of numbers/letters representing the row and column of the letter in the Polybius Square.  To decode a message, the pairs of numbers in the ciphertext are matched to the corresponding letters in the Polybius Square based on their row and column positions.

Myszkowski Transposition involves rearranging the plaintext characters based on a keyword or phrase. The keyword determines the order of rearrangement. Repeated letters in the keyword are numbered sequentially to indicate their order in the transposition. The plaintext is written out in rows, with the length of each row determined by the length of the keyword. Then, the columns are rearranged according to the numerical order of the keyword letters. After rearranging the columns, the characters are read off from the columns in the alphabetical order of the keyword. The resulting ciphertext is the rearranged characters of the plaintext. To decrypt the ciphertext, the process is reversed. The keyword is used to determine the original order of the columns, and the characters are then read off column by column to recover the plaintext.

EXAMPLES FROM EXECUTION
1. Polybius Square Cipher
   
![image](https://github.com/leonitaas/DataSecurity/assets/116391183/30c5b500-66fa-4265-ad74-ed17fb69d454)
![image](https://github.com/leonitaas/DataSecurity/assets/116391183/12a116cc-e85e-4362-b237-09c39c695fbf)

3. Myszkowski Transposition Cipher
   
![image](https://github.com/leonitaas/DataSecurity/assets/116465243/93592512-e17f-4e74-96d6-fb81312587ea)
![second](https://github.com/leonitaas/DataSecurity/assets/116763240/9ec8b055-d004-4dd4-8272-45ccadac49ff)





# Confidential
This project is developed from the authors below with full rights.

# Authors

[Elda Qollaku](https://github.com/eldaaqollaku)


[Leonita Sinani](https://github.com/leonitaas)


[Linda Hasanaj](https://github.com/Linda-Hasanaj)


[Leutrim Morina](https://github.com/LeutrimMorina13)






