while True:
	try:
		a = float(input("First: "))
		b = float(input("Second: "))
		c = float(input("Third: "))
		break
	except ValueError:
		print("Invalid input")

print(max(c, max(a,b)))
