while True:
	try:
		num = int(input("Enter input: "))
		break
	except ValueError:
		print("Oooopppssss...")

def reverse(num):
	if num < 10 and num >= 0:
		return str(num)

	return str(num%10) + str(reverse(int(num/10)))

print(reverse(abs(num)))
