while True:
	try:
		first = int(input("Enter input: "))
		second = int(input("Enter input: "))
		break
	except ValueError:
		print("Invalid input")

counter = min(first, second)
while counter > 0:
	if first % counter == 0 and second % counter == 0:
		print("EBOB: " + str(counter))
		break
	counter -= 1
