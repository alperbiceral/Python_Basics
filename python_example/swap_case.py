text = input("Enter input: ")
list = []

for i in range(len(text)):
	list.append(text[i])

for i in range(len(list)):
	if list[i].isupper():
		list[i] = list[i].lower()
	elif list[i].islower():
		list[i] = list[i].upper()


text = ""
for i in range(len(list)):
	text += list[i]

print(text)
