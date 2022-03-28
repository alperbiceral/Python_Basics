fibo = [1, 1]

for i in range(2, 11):
	fibo.append(fibo[i-1] + fibo[i-2])

print(fibo)
