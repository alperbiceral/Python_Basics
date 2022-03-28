import sys

text = input("Enter the string: ")

print("\nIs it palindrome?")
for i in range(int(len(text) / 2)):
	if text[i] != text[len(text) - i - 1]:
		print("NO")
		sys.exit()

print("YES")
