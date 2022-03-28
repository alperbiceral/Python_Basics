import math

radius = -1

while radius < 0:
	try:
		radius = float(input("Insert the radius: "))
	except ValueError:
		print("Please type a numeric character.\n")

print("Area of the circle is: " + str((radius**2)*math.pi))
