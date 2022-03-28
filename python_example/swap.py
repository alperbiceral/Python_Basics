while True:
	try:
		first = float(input("First: "))
		second = float(input("Second: "))
		break
	except ValueError:
		print("Invalid input.")

temp = first
first = second
second = temp

print("First: " + str(first))
print("Second: " + str(second))
