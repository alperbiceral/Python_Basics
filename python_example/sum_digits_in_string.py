text = input("Enter input: ")
sum = 0

for i in range(len(text)):
	if text[i].isalnum() and not text[i].isalpha():
		sum += int(text[i])

print(sum)
