list = []
print("0 to quit")
while True:
	try:
		newInput = float(input("Add this one: "))

		if newInput == 0:
			break

		list.append(newInput)
	except ValueError:
		print("Invalid input")


sum = 0
for i in range(len(list)):
	sum += list[i]

print(sum)
