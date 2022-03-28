text = input("Enter input: ")
result = ""

for i in range(len(text)):
	if text[i].isupper():
		result += text[i]

print(result)
