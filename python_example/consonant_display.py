str = input("Enter input: ")
list = []

for i in range(len(str)):
	if str[i].lower() != "a" and str[i].lower() != "e" and str[i].lower() != "i" and str[i].lower() != "o" and str[i].lower() != "u" and str[i].isalpha():
		list.append(str[i])

print(list)
