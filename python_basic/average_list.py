list = []
while True:
	try:
		list.append(int(input("Enter input (0 to quit): ")))
		if list[len(list) - 1] == 0:
			break
	except ValueError:
		print("Invalid input")

sum = 0
for i in range(len(list)):
	sum += list[i]
aver = int(sum / (len(list) - 1))

print(aver)
