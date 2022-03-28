while True:
	try:
		num = int(input("Enter input: "))
		break
	except ValueError:
		print("Invalid input")

def factorial(num):
	if num <= 1:
		return 1

	return num*factorial(num-1)


print(factorial(num))
