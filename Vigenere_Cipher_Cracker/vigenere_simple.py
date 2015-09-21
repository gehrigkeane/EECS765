#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Gehrig Keane
#	2727430
#	Mini-project 1
#	vigenere_simple.py - simple vigenere encryption/decryption tool
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Simple Function for rebuilding strings
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def rebuild(word):
	word = [chr(i+97) for i in word]
	return str(''.join(word))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Gather Integer + String Input
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
decision = ""
while decision < 1 or decision > 2:
	print "Encrypt string: 1"
	print "Decrypt string: 2"
	decision = int(raw_input("\n: "))

text = raw_input("\nEnter text: ")
text = text.replace(" ","").strip('\r\n').lower()

key = raw_input("\nEnter key: ")
key = key.replace(" ","").strip('\r\n').lower()

print ("\nText: " + text)
print ("Key: " + key)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#**************************************************
#	Encryption
#		- Converts plain_text to an integer tuple
#		- Converts key to an integer tuple
#		- Encrypts each char of plain_text
#**************************************************
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def encrypt(plain_text, key):
	plain_text = [(ord(c) - 97) for c in plain_text]
	int_key = [(ord(c) - 97) for c in key]
	return [(plain_text[i] + int_key[i%len(int_key)])%26 for i in range(len(plain_text))]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#**************************************************
#	Decryption
#		- Converts cipher_text to an integer tuple
#		- Converts key to an integer tuple
#		- Decrypts each char of cipher_text
#**************************************************
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def decrypt(cipher_text, key):
	cipher_text = [(ord(c) - 97) for c in cipher_text]
	int_key = [(ord(c) - 97) for c in key]
	return [(cipher_text[i] - int_key[i%len(int_key)])%26 for i in range(len(cipher_text))]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#**************************************************
#	I/O
#**************************************************
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if decision == 1:
	text = encrypt(text, key)
	print ("Encrypted text: " + rebuild(text))
elif decision == 2:
	text = decrypt(text, key)
	print ("Decrypted text: " + rebuild(text))
