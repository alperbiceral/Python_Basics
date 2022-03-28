num = int(input("Enter input: "))
sum = 0

for i in range(1, num):
	if num % i == 0:
		sum += i

if num == sum:
	print("PERFECT NUMBER")
else:
	print("No")
