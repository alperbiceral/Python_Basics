text = input("Enter input: ")

while True:
	try:
		num = int(input("How many characters do you want? "))
		break
	except ValueError:
		print("Invalid input")

print(text[:num])
