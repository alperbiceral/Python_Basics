list = [5, 9, 3, 7, 6]

print(list)

for i in range(len(list)):
	# keep the values to compare and replace
	index = i
	tmp = list[i]

	for j in range(i + 1, len(list)):
		if tmp > list[j]:
			# update the temporary values if necessary
			index = j
			tmp = list[j]
	# swap places
	tmp = list[index]
	list[index] = list[i]
	list[i] = tmp

print()
print(list)
