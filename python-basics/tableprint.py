tableData = [['apples', 'oranges', 'cherries', 'banana'],
		['Alice', 'Bob', 'Carol', 'David'],
		['dogs', 'cats', 'moose', 'goose']]

print("same category at the horizontal")
for i in range(len(tableData)):
	for j in range(len(tableData[i])):
		print(tableData[i][j].rjust(10), end="")
	print()

print()

print("same category at the vertical")
for i in range(len(tableData[0])):
	for j in range(len(tableData)):
		print(tableData[j][i].rjust(10), end="")
	print()
