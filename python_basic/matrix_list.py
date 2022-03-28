list = [1, 2, 3, 4]

for i in range(len(list)):
	list[i] = []
	for j in range(i + 1):
		list[i].append("X ")
	for j in range(len(list) - (i + 1)):
		list[i].append("O ")

for i in range(len(list)):
	for j in range(len(list[i])):
		print(list[i][j], end="")
	print()
