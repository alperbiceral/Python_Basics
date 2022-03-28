length = 8

for i in range(1, length * 2, 2):
	print(" " * int((length * 2 - i - 1) / 2), end="")
	print("*" * i, end="")
	print(" " * int((length * 2 - i - 1) / 2))

for i in range(length * 2 - 1, 0, -2):
	print(" " * int((length * 2 - i - 1) / 2), end="")
	print("*" * i, end="")
	print(" " * int((length * 2 - i - 1) / 2))
