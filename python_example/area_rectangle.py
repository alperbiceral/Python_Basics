first = -1
second = -1
while first < 0 or second < 0:
	try:
		first = float(input("Insert the first side: "))
		second = float(input("Insert the second side: "))
	except ValueError:
		print("You cannot type non-numeric characters.\n")

print("Area of the rectangle is: " + str(first*second))
