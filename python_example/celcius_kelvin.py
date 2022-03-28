while True:
	try:
		value = float(input("Enter input: "))
		break
	except ValueError:
		print("Invalid input")

print(value + 273.15)
