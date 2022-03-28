while True:
	try:
		principal = float(input("Principal amount: "))
		rate = float(input("Interest Rate (for a year): "))
		time = float(input("Time (years): "))
		break
	except ValueError:
		print("Invalid input")

print("Interest earned after " + str(time) + " years is " + str(principal*rate*time/100.0))
