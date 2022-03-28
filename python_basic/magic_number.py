num = int(input("Enter input: "))

def magic_check(num):
	if num < 10:
		return num

	return magic_check(int(num / 10)) + (num % 10)

while True:
	num = magic_check(num)
	if num < 10:
		print(num)
		break

if num == 1:
	print("MAGIC NUMBER")
else:
	print("NOT MAGIC NUMBER")
