while True:
	ch = input("Enter only one character: ")

	if len(ch) == 1:
		break

if ch.isalnum():
	print(ch + " is not a special character")
else:
	print(ch + " is a special character")
