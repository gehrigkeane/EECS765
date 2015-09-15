#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Gehrig Keane
#	2727430
#	vigenere.py - polished python script
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import time
tstart = time.time()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Simple Function for rebuilding strings
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def rebuild(word):
	word = [chr(i+97) for i in word]
	return str(''.join(word))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Gather Integer + String Input
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
key_len = raw_input("\nEnter key length: ")
key_len = int(key_len)

word_len = raw_input("\nEnter word length: ")
word_len = int(word_len)

cipher_text = raw_input("\nEnter cipher text: ")
cipher_text = cipher_text.strip('\r\n').lower()

print ("\n\nKey length: " + str(key_len))
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
#	Convert strings to integer tuples
#		- Zero's ints with ord(c) - 97
#		- Increases decryption efficiency
#		  by preprocessing char's and ascii
#		  values
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
uniLines = [[(ord(c) - 97) for c in word] for word in lines]

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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Generate key for each word in list
#		- Generates key based on key_len
#		- Decrypts first word with generated key
#		- Checks if word is correct
#		- If yes - break and finish
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for word in uniLines:
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#		Calculate key from dictionary word
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	key = [(ford[i] - word[i])%26 for i in range(key_len)]

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#		Decrypt first word
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	p = [(ford[i] - key[i%key_len])%26 for i in range(len(ford))]

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#		Did we succeed?
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	if p == word:
		print ("\nThe key: " + rebuild(key))
		print ("The first word: " + rebuild(word))
		p = [(cipher_text[i] - key[i%key_len])%26 for i in range(len(cipher_text))]
		print ("The decrypted string: " + rebuild(p))
		break;

end = time.time()
decrypt_time = end - start
print ("\nPreprocessing time: " + str(preproc_time))
print ("Decryption time: " + str(decrypt_time))
print ("Total time: " + str(time.time() - tstart))
