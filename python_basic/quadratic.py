while True:
	try:
		a = int(input("a: "))
		b = int(input("b: "))
		c = int(input("c: "))
		break
	except ValueError:
		print("Invalid input")

print("\n" + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0\n\n")

dis = (b**2-4*a*c)**(0.5)

if dis == 0:
	discriminant1 = (-b)/(2*a)
	print(discriminant1)
else:
	discriminant1 = -b-(b**2-4*a*c)**(0.5)/(2*a)
	discriminant2 = -b+(b**2-4*a*c)**(0.5)/(2*a)
	print(discriminant1)
	print(discriminant2)
