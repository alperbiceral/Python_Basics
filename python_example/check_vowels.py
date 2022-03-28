str = input("Enter input: ")

for i in range(len(str)):
	if str[i].lower() == "a" or str[i].lower() == "e" or str[i].lower() == "i" or str[i].lower() == "o" or str[i].lower() == "u":
		print("string contains vowel\n")
		break

if str[0] == "a" or str[0] == "e" or str[0] == "i" or str[0] == "o" or str[0] == "u":
	print("the first character of the string is vowel\n")
else:
	print("the first character of the string is NOT vowel\n")
