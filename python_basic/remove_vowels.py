import re
text = input("Enter input: ")
list = []

list = re.split("a|e|i|o|u|A|E|I|İ|O|U", text)

text = ""
for i in range(len(list)):
	text += list[i]

print(text)
