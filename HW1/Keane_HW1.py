#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Gehrig Keane
#	2727430
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cipher_text = raw_input("\nEnter cipher text: ")
cipher_text = cipher_text.strip(' \r\n').lower()

key = raw_input("\nEnter key: ")
key = key.strip(' \r\n').lower()
print("\n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Traditional Shifting Tool (Caesar)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Functional Caesar Decoder
# for k in range(26):
# 	unic = [(ord(c) - 97) for c in cipher_text if ord(c)!=32]
# 	unic = [(i-k)%26 for i in unic]
# 	unic = [(chr(i + 97)) for i in unic]
# 	print (str(k) + ": " + ''.join(unic))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Frequency Analysis Tool
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Frequency
# for k in range(26):
# 	i = 0;
# 	for c in cipher_text:
# 		if chr(k + 97) == c:
# 			i += 1
# 	print (chr(k + 97) + "=" + str(i))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Reverse Shifting Tool
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reverse shift algorithm
# for i in range(26):
# 	cipher_text1 = [(25 - (ord(c)-97)) for c in cipher_text if ord(c)!=32]
# 	cipher_text1 = [(k-i)%26 for k in cipher_text1]
# 	cipher_text1 = [chr(a+97) for a in cipher_text1]
# 	print ("Shift " + str(i) + ": " + ''.join(cipher_text1))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	Replacement Tool
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# cipher_text = raw_input("\nEnter cipher text: ")
# cipher_text = cipher_text.strip('\r\n').lower()

# find = raw_input("\nEnter find char: ")
# find = find.strip('\r\n').lower()

# replace = raw_input("\nEnter replace char: ")
# replace = replace.strip('\r\n').lower()

# print cipher_text.replace(find, replace)