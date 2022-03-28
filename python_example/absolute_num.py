while True:
	try:
		num = float(input("Enter the number: "))
		break
	except ValueError:
		print("Invalid input")

if num > 0:
	print(num)
elif num < 0:
	print(-num)
elif num == 0:
	# user may be enter -0 as the input
	print(0)
