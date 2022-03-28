while True:
	try:
		choice = float(input("Fahrenheit -> Celcius(0) or Celcius -> Fahrenheit(1): "))
		if choice == 0 or choice == 1:
			value = float(input("Enter the value: "))
		else:
			print("enter 0 or 1")
			continue
		break
	except ValueError:
		print("Invalid input")

if choice == 0:
	result = (value - 32) / 1.8
else:
	result = value * 1.8 + 32

print(result)
