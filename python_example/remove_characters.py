import re

text = input("Enter input: ")
ch = input("Enter removing character: ")

list = re.split(ch, text)

text = ""
for i in range(len(list)):
	text += list[i]

print(text)
