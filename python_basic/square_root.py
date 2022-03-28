
while True:
	try:
		num = float(input("Insert the number: "))
		break
	except ValueError:
		print("Please type a numeric character\n")

num = num ** 0.5

print("Square root of the number is: " + str(num))
