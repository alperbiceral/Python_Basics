divisor = 0
while divisor == 0.0:
	try:
		divident = float(input("Insert the divident: "))
		divisor = float(input("Insert the divisor: "))

		if divisor == 0.0:
			print("You cannot divide by 0\n")
	except ValueError:
		print("Cannot convert to float.")
		continue

print("Divison of " + str(divident) + " by " + str(divisor) + " is " + str(divident/divisor))
