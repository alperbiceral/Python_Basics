length = 8

print(" " * int((2 * length - 1) / 2) + "*")
for i in range(3, 2 * length, 2):
	print(" " * int((2 * length - i) / 2), end="")
	print("*", end="")
	print(" " * (i - 2), end="")
	print("*")

for i in range(1, length + 1):
	print("* ", end="")
print()
