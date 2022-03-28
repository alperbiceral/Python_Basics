while True:
	try:
		num = float(input("Input: "))
		break
	except ValueError:
		print("Invalid input")

if num >= 0:
	if int(num**(0.5)) == num**(0.5):
		print(str(num) + " is perfect square :)")
	else:
		print(str(num) + " is not perfect square :(")
else:
	print("Negative numbers cannot be perfect squares. Soorrrryyy.")
