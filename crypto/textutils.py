# Description:
# testutils.py contains simple text-related
# helper functions
# 
# Author:
# Calvin Yeung (dbydt)

# shifts character without bounds (dangerous)
def char_shift(character, shift):
	return chr(ord(character) + shift)

# shifts upper or lower case characters with wrap
def normalized_char_shift(character, shift):
	ascii = ord(character) + shift
	
	if(character.isupper()):
		while ascii < ord('A'):
			acsii += 26
		while ascii > ord('Z'):
			ascii -= 26
	elif(character.islower()):
		while ascii < ord('a'):
			ascii += 26
		while ascii > ord('z'):
			ascii -= 26
	
	return chr(ascii)