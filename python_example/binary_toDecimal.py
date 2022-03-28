binary = input("Enter input: ")
mul_const = 1
result = 0

for i in range(len(binary)-1, -1, -1):
	result += int(binary[i])*mul_const
	mul_const *= 2

print(result)
