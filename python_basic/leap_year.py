while True:
	try:
		year = int(input("Enter year: "))
		break
	except ValueError:
		print("Invalid input.")

if year % 4 == 0:
	print(str(year) + " is leap year :)")
else:
	print(str(year) + " is not leap year :(")
