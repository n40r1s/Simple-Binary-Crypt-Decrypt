def decrypt():
	a_binary_string=input("Enter your binary\n")
	binary_values = a_binary_string.split()   #Split string on whitespace
	ascii_string = ""
	for binary_value in binary_values:
		an_integer = int(binary_value, 2) #Convert to base 2 decimal integer
		ascii_character = chr(an_integer) #Convert to ASCII character
		ascii_string += ascii_character   #Append character to `ascii_string`
	print(ascii_string)
decrypt()
