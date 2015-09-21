#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Gehrig Keane
#	2727430
#	Mini-project 1
#	crack_slow.py - testing suite (basically the code scratchpad)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import marisa_trie
from itertools import product
import time
from string import ascii_lowercase
tstart = time.time()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#				Gather Integer + String Input
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cipher_text = raw_input("\nEnter cipher text: ")
cipher_text = cipher_text.replace(" ","").strip('\r\n').lower()

key_len = raw_input("\nEnter key length: ")
key_len = int(key_len)

word_len = raw_input("\nEnter word length: ")
word_len = int(word_len)

print ("\nKey length: " + str(key_len))
print ("Word length: " + str(word_len))
print ("Cipher text: " + str(cipher_text))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#**************************************************
#	Preprocessing
#**************************************************
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
start = time.time()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Convert dict.txt to list
#		- Only accepts word of length word_len
#		- Converts all word to lowercase
#		- Strips whitespace 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
lines = [line.rstrip('\r\n').lower() for line in open('dict.txt') if len(line.rstrip('\r\n').lower())==word_len]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Convert list to trie structure
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
trie = marisa_trie.Trie(lines);

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Extract first word from cipher text
#		- Converts word to Zero'd integer tuple
#		- Increases decryption efficiency
#		  by preprocessing char's and ascii
#		  values 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ford = [(ord(c) - 97) for c in cipher_text[:word_len]]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Convert entire cipher text for later
#		- Converts cipher text to integer tuple
#		- Increases ease of use for decryption
#		  of the whole cipher text when key is 
#		  located
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cipher_text = [(ord(c) - 97) for c in cipher_text]

end = time.time()
preproc_time = end - start

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#**************************************************
#	Decryption
#**************************************************
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
start = time.time()

for combo in product(ascii_lowercase, repeat=key_len):
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#		Calculate key int tuple
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	key = [(ord(c) - 97) for c in combo]
	
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#		Decrypt first word
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	p = [(ford[i] - key[i%key_len])%26 for i in range(len(ford))]
	uni_p = [chr(i+97) for i in p]

	if unicode(''.join(uni_p)) in trie:
		print ("\nKey = " + ''.join(combo))
		full_p = [(cipher_text[i] - key[i%key_len])%26 for i in range(len(cipher_text))]
		full_p = [chr(i+97) for i in full_p]
		print ("Plaintext = " + ''.join(full_p))

end = time.time()
decrypt_time = end - start
print ("\nPreprocessing\t: " + str(preproc_time))
print ("Decryption\t\t: " + str(decrypt_time))
print ("Total\t\t\t: " + str(time.time() - tstart))
