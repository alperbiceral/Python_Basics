while True:
	try:
		first = int(input("Enter a number: "))
		second = int(input("Enter a number: "))
		break
	except ValueError:
		print("Invalid input")

counter = max(first, second)
while True:
	if counter % first == 0 and counter % second == 0:
		print("EKOK: " + str(counter))
		break
	counter += 1
