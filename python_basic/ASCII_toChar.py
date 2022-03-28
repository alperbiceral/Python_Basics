while True:
	try:
		num = int(input("Enter input: "))
		break
	except ValueError:
		print("Invalid input")

print(chr(num))
