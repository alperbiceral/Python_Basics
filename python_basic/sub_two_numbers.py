while True:
	try:
		first = float(input("Insert the first number: "))
		second = float(input("Insert the second number: "))
		break
	except ValueError:
		print("Type a valid input\n")

print("Subtraction of " + str(first) + " and " + str(second) + " is " + str(first-second))
