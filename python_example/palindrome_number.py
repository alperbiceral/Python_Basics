import sys
num = input("Enter input: ")

for i in range(int(len(num) / 2)):
	if int(num[i]) != int(num[len(num) - i - 1]):
		print("NO")
		sys.exit()

print("PALINDROME NUMBER")
