text = input("Enter input: ")
i = 0
while i < len(text):
	if not text[i].isalnum():
		text = text[:i] + text[i+1:]
		i -= 1
	i += 1

print(text)
