while True:
	try:
		num = abs(int(input("Enter input: ")))
		break
	except ValueError:
		print("Invalid input")

while num >= 10:
	num = int(num/10)

print(num)
