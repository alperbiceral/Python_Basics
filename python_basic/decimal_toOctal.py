decimal = int(input("Enter input: "))
octal = []

while decimal > 0:
	octal.append(decimal % 8)
	decimal = int(decimal / 8)

for i in range(len(octal)-1, -1, -1):
	print(octal[i], end="")
print()
