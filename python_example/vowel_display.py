str = input("Enter input: ")
list = []

for i in range(len(str)):
	if str[i].lower() == "a" or str[i].lower() == "e" or str[i].lower() == "i" or str[i].lower() == "o" or str[i].lower() == "u":
		list.append(str[i])

print(list)
