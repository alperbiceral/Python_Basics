is_prime = True
while True:
	try:
		num = int(input("Enter input: "))
		break
	except:
		print("Invalid input")

for i in range(2, num):
	if num % i == 0:
		is_prime = False
		print("NOT prime")
		break

if is_prime:
	print("prime")
