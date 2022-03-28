num = input("Enter input: ")
fact_sum = 0

for i in range(len(num)):
	temp_fact = 1
	for j in range(1, int(num[i])+1):
		temp_fact *= j
	fact_sum += temp_fact

if fact_sum == int(num):
	print("STRONG NUMBER")
else:
	print("NO")
