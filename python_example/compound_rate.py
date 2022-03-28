while True:
	try:
		principal = float(input("Principal amount: "))
		rate = float(input("Interest Rate (e.g. 0.05): "))
		compound = float(input("Number of compounding for a year: "))
		time = float(input("Total number of years: "))
		break
	except ValueError:
		print("Invalid input")

total = principal*(1+rate/compound)**(compound*time)
print("\nTotal Money: " + str(total) + "\nCompound Interest: " + str(total-principal))
