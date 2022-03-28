primes = []
while True:
	try:
		num = int(input("Enter input: "))
		break
	except ValueError:
		print("Invalid input")

for i in range(2, num):
	# just look at the dividors
	if num % i != 0:
		continue

	# differentiate if the is prime or not
	is_prime = True
	for j in range(2, i):
		if i % j == 0:
			is_prime = False
			break
	if is_prime: # add i to the list if it is prime
		primes.append(i)

print(primes)
