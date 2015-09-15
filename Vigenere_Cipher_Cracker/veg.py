#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Gehrig Keane
#	2727430
#	veg.py - testing suite (basically the code scratchpad)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#import marisa_trie
#from itertools import product
import time
#from string import ascii_lowercase

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#				Gather Integer + String Input
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
key_len = raw_input("\nEnter key length: ")
key_len = int(key_len)

word_len = raw_input("\nEnter word length: ")
word_len = int(word_len)

cipher_text = raw_input("\nEnter cipher text: ")
cipher_text = cipher_text.strip('\r\n').lower()

print ("\nKey length: " + str(key_len))
print ("Word length: " + str(word_len))
print ("Cipher text: " + str(cipher_text))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#			Reading Lines into the list
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
start = time.time()

#	if x == y --> .rstrip('\r\n') --> .lower() --> append
lines = [line.rstrip('\r\n').lower() for line in open('dict.txt') if len(line.rstrip('\r\n').lower())==word_len]

#	For every word => for every char in word => make ascii - 97
uniLines = [[(ord(c) - 97) for c in word] for word in lines]

ford = [(ord(c) - 97) for c in cipher_text[:word_len]]

cipher_text = [(ord(c) - 97) for c in cipher_text]

#	word = [(ord(c) - 97) for c in "caesar"]
#	For every word calculate key
#keys = [[(ford[i] - word[i])%26 for i in range(key_len)] for word in uniLines]
def rebuild(word):
	word = [chr(i+97) for i in word]
	return str(''.join(word))

for word in uniLines:
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#		Calculate key from dictionary word
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	key = [(ford[i] - word[i])%26 for i in range(key_len)]

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	#				Decrypt first word
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	p = [(ford[i] - key[i%key_len])%26 for i in range(len(ford))]

	if p == word:
		print ("The key is: " + rebuild(key))
		print ("The first word: " + rebuild(word))
		p = [(cipher_text[i] - key[i%key_len])%26 for i in range(len(cipher_text))]
		print ("The decrypted string: " + rebuild(p))
		break;



# print ("Key: " + str(key))
# print ("Plain: " + str(p))
#p = [i - key[] for i in len(ford)]


# for word in lines:
# 	t = []
# 	for i in word:
# 		t.append(ord(i) - 65)
# 	uniLines.append(t)

#print ("Keys: " + str(key))
# print ("First word: " + str(ford))

end = time.time()
print ("File time: " + str(end - start))
#print (lines)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#			Depositing List into a Trie
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# start = time.time()
# trie = marisa_trie.Trie(lines)
# end = time.time()
# print ("Trie time: " + str(end - start))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#			Decryption Jargin
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# key=""
# # for word in lines:
# for word in lines:
# 	for i in range(key_len):
# 		c = ord(cipher_text[i]) - 65
# 		k = ord(word[i]) - 65
# 		key = str(key) + chr( ( (c-k) % 26 ) + 65 )

# word = 'education'
# #Gather Key from Dictionary




# print (key)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#			Decryption Jargin
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def decryptAll(key, cipher):
# 	i = 0
# 	p = []
# 	while i < len(cipher):
# 		for j in key:
# 			if i >= len(cipher):
# 				break
# 			c = ord(cipher[i]) - 65
# 			k = ord(j) - 65
# 			p.append( chr( ( (c-k) % 26 ) + 65 ) )
# 			i += 1
# 	return ''.join(p)

# def decryptWord(key, cipher_text):
# 	i = 0
# 	p = []
# 	while i < len(cipher_text):
# 		for j in key:
# 			if i >= len(cipher_text):
# 				break
# 			c = ord(cipher_text[i]) - 65
# 			k = ord(j) - 65
# 			p.append( chr( ( (c-k) % 26 ) + 65 ) )
# 			i += 1
# 			#print ( chr( ( ord(i) + ord(j) ) % 25 ) )
# 			#print chr( ord( (cipher_text[i]+key[j]) % 25 ) )
# 	p = ''.join(p).lower()
# 	if unicode(p, "utf-8") in trie:
# 		return p
# 	else:
# 		return False

# start = time.time()
# for combo in product(ascii_lowercase, repeat=key_len):
# 	if decryptWord(combo, cipher_text[:word_len]):
# 		print ("\nKey = " + ''.join(combo))
# 		print ("Plaintext = " + decryptAll(combo, cipher_text))
# 		break
# end = time.time()
# print ("Key time: " + str(end - start))



# def decryptAll(key, cipher):
# 	i = 0
# 	p = []
# 	while i < len(cipher):
# 		for j in key:
# 			if i >= len(cipher):
# 				break
# 			c = ord(cipher[i]) - 65
# 			k = ord(j) - 65
# 			p.append( chr( ( (c-k) % 26 ) + 65 ) )
# 			i += 1
# 	return ''.join(p)

# def decryptWord(key, cipher_text):
# 	i = 0
# 	p = []
# 	for 
# 	while i < len(cipher_text):
# 		for j in key:
# 			if i >= len(cipher_text):
# 				break
# 			c = ord(cipher_text[i]) - 65
# 			k = ord(j) - 65
# 			p.append( chr( ( (c-k) % 26 ) + 65 ) )
# 			i += 1
# 			#print ( chr( ( ord(i) + ord(j) ) % 25 ) )
# 			#print chr( ord( (cipher_text[i]+key[j]) % 25 ) )
# 	p = ''.join(p).lower()
# 	if unicode(p, "utf-8") in trie:
# 		return p
# 	else:
# 		return False

# start = time.time()
# for combo in product(ascii_lowercase, repeat=key_len):
# 	if decryptWord(combo, cipher_text[:word_len]):
# 		print ("\nKey = " + ''.join(combo))
# 		print ("Plaintext = " + decryptAll(combo, cipher_text))
# 		break
# end = time.time()
# print ("Key time: " + str(end - start))


#print (trie.items())
#print (lines)
#print (trie.items())

# start = time.time()
# print ("REEXPORTATIONS: " + str(u'reexportations' in trie))
# end = time.time()
# print ("Search time: " + str(end - start))
