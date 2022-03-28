text = input("Enter input: ")
num_list = []

for i in range(len(text)):
	if text[i].isalnum() and not text[i].isalpha():
		num_list.append(int(text[i]))

print(num_list)

