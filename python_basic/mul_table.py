while True:
	try:
		num = int(input("Enter input: "))
		break
	except ValueError:
		print("Invalid input.")

for i in range(1, 11):
	print(str(num) + " X " + str(i) + " = " + str(num*i))
