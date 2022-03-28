value = 0.0
choice = 0
while True:
	try:
		choice = int(input("KM -> Miles(0) or Miles -> KM(1) "))
		if choice != 0 and choice != 1:
			continue
		else:
			value = float(input("Insert the value you want to convert: "))
			break
	except ValueError:
		print("Invalid input")

if choice == 0:
	result = value*0.621371
	print(str(value) + " KMs is equal to " + str(result) + " miles.")
elif choice == 1:
	result = value*1.60934
	print(str(value) + " Miles is equal to " + str(result) + " KM.")
