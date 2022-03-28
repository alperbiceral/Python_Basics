while True:
	try:
		operator = input("Add(+), Sub(-), Mul(*), Div(/)")
		first = float(input("First: "))
		second = float(input("Second: "))
		break
	except ValueError:
		print("Invalid input")

if operator == "+":
	print(str(first+second))
elif operator == "-":
	print(str(first-second))
elif operator == "*":
	print(str(first*second))
elif operator == "/":
	try:
		print(str(first/second))
	except ZeroDivisionError:
		print("Cannot divide to zero, sorry...")
else:
	print("Improper input...\nQuiting...")
