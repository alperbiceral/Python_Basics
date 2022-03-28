length = 8

for i in range(1, length+1):
	print("*" * i)

print()

for i in range(1, length+1):
	print(" " * (length - i), end="")
	print("*" * i)

print()

for i in range(1, 2*length, 2):
	print(" " * int((2 * length - i - 1) / 2), end="")
	print("*" * i, end="")
	print(" " * int((2 * length - i - 1) / 2))
