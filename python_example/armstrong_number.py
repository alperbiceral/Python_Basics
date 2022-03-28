num = input("Enter input: ")
sum = 0
exp = len(num)

for i in range(len(num)):
	sum += int(num[i])**exp

if int(num) == sum:
	print("ARMSTRONG NUMBER")
else:
	print("No")
