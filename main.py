from EncoderDecoder import EncoderDecoder

ed = EncoderDecoder()

input_1 = "1=> Check if decoder returns original string.\n"
input_2 = "2=> Get help.\n"
input_3 = "3=> Exit.\n"
message = "\nEnter input:\n"+input_1+""+input_2+""+input_3

print(message)

while(True):
	while(True):
		
		user_input = int(input())
		if user_input in (1,2,3):
			break
		else:
			print("Invalid input")

	if(user_input==1):
		string_to_encode = input("Enter string to encode.\n")
		string_to_compare = input("Enter string to compare it with it.\n")
		try:
			encoded_array = ed.encode(string_to_encode)
			decoded_string = ed.decode(encoded_array)
			strings_match = decoded_string == string_to_compare
			if strings_match:
				print("Encoded/decoded string matches input string.\n")
			else:
				print("Encoded/decoded string does not match input string.\n")
			print("Press 1 to compare more strings")
		except:
			continue
	
	elif(user_input==2):
		print(message)
	
	elif(user_input==3):
		print("Goodbye!")
		break
		
	