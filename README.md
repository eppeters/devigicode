devigicode
==========

vigenere cipher decoder

Summary
-------

To use devigicode in its current stage, you must know the keyword length of the Vig&#232nere enciphered text.

devigicode uses a given key length to return a number of the most probable plaintexts for a given ciphertext. The possible decryptions are scored by how many words in the words.txt they contain. So, for example, if you have set the program to print 5 "decryptions," it *may* print 15 possible decryptions (for example, 3 containing 10 words, 5 containing 2 words, and 8 containing 1 word).

Development Notes
-----------------
