factors = []
while True:
	try:
		num = int(input("Enter input: "))
		break
	except ValueError:
		print("Invalid input")

for i in range(1, num+1):
	if num % i == 0:
		factors.append(i)

print(factors)
