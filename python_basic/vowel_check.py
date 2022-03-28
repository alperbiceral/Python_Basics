ch = "a"
while True:
	ch = input("Enter a character: ").lower()

	if len(ch) == 1:
		break


if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
	print("vowel")
else:
	print("consonant")
