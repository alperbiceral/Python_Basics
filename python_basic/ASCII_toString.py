nums = []
while True:
	try:
		nums.append(int(input("Enter ASCII no. (0 to exit): ")))
		if nums[len(nums)-1] == 0:
			break
	except ValueError:
		print("Invalid input")

for i in range(len(nums)):
	print(chr(nums[i]), end=" ")
print()
