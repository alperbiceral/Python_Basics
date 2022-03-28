while True:
	try:
		num = int(input("Enter input: "))
		break
	except ValueError:
		print("Invalid input.")

if num % 2 == 0:
	print("EVEN")
else:
	print("ODD")
