def crypt():	
	a_string = input("Enter the string you want to crypt\n")
	a_byte_array = bytearray(a_string, "utf8")
	byte_list = []
	for byte in a_byte_array:
		binary_representation = bin(byte)
		byte_list.append(binary_representation)
	for i in range(0,len(byte_list)):
		byte_list[i]=byte_list[i].replace('b', '')
		print(byte_list[i]," ",end = '')
crypt()
	

