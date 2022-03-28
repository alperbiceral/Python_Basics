while True:
	try:
		first = float(input("Insert the first number: "))
		second = float(input("Insert the second number: "))
		break
	except ValueError:
		print("Invalid input!")

print("Multiplication of " + str(first) + " and " + str(second) + " is " + str(first*second))
