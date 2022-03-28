octal = input("Enter input: ")
constant = 1
decimal = 0

for i in range(len(octal)-1, -1, -1):
	decimal += int(octal[i]) * constant
	constant *= 8

print(decimal)
