# Author: Anish Gadekar

class EncoderDecoder:

	"""
	The encode function takes an input sentence of type string.
	returns: An array of encoded integers representing input sentence.
	"""
	def encode(self, sentence):
		# Ensure sentence is a string
		if not isinstance(sentence, str):
			print("Input not a string.")
			print("Please enter a string")
			raise

		encoded_array = []

		# Encoding is performed on 4 consecutive characters from the input.
		wordArray= [sentence[i:i+4] for i in range(0, len(sentence), 4)]
		for word in wordArray:
			encoded_word=0
			base = 1
			for char in word:
				ascii_value = ord(char)
				multiplier = 1
				while(ascii_value!=0):
					bit = ascii_value&1
					encoded_word += bit*base*multiplier
					multiplier *= 16
					ascii_value = ascii_value >> 1
				base *= 2
			encoded_array.append(encoded_word)		

		return encoded_array 

	"""
	The decode function takes an array of integers containing encoded integers.
	returns: A string representing original sentence.
	"""
	def decode(self, encoded_array):
		# Ensure encoded_array contains only integers
		for encoded_value in encoded_array:
	 		if not isinstance(encoded_value, int):
	 			print("Invalid input.")
	 			print("Please enter only integer values for encoded array.")
	 			raise

		sentence = ""
		# Each encoded_word represents a string of length 4.
		for encoded_word in encoded_array:
			exponent = 0
			base = 1
			decoded_decimal = 0

			# Logic to obtain decimal value of encoded_word.
			while(encoded_word>0):
				bit = encoded_word%2
				decoded_decimal += bit*(2**exponent)*base
				if(exponent==24):
					exponent=0
					base*=2
				else:
					exponent+=8
				encoded_word = encoded_word//2

			word = ""
			ascii_value = 0
			multiplier = 1

			# Logic to decode encoded_word using the decimal value of encoded_word.
			while(decoded_decimal>0):
				if(multiplier==2**8):
					word = word + chr(ascii_value)
					multiplier = 1
					ascii_value = 0
				bit = decoded_decimal&1
				ascii_value += multiplier*bit
				multiplier = multiplier*2
				decoded_decimal = decoded_decimal >> 1
			if(ascii_value!=0):
				word = word + chr(ascii_value)

			sentence = sentence + word
		return sentence