base = -1
height = -1

while base < 0 or height < 0:
	try:
		base = float(input("Insert the base: "))
		height = float(input("Insert the height: "))
	except ValueError:
		print("You cannot insert a non-numeric character.\n")

print("Area of the triangle is: " + str(base*height/2.0))
