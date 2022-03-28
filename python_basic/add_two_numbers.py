while True:
	try:
		first = int(input("Insert the first number: "))
		second = int(input("Insert the second number: "))
		break
	except ValueError:
		print("Please type a valid input\n")

print("The sum of " + str(first) + " and  " + str(second) + " is: " + str(first+second))
