while True:
	try:
		num = abs(int(input("Enter input: ")))
		break
	except ValueError:
		print("Invalid input.")

def digit_sum(num):
	if num == 0:
		return 0

	return (num % 10) + digit_sum(int(num / 10))

print(digit_sum(num))
