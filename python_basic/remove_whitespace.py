text = input("Enter input: ")

list = text.split(" ")

text = ""
for i in range(len(list)):
	text += list[i]

print(text)
