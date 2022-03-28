list1 = [[1, 2], [3, 4]]
list2 = [[6, 7], [8, 9]]
list3 = [[], []]

print("List1: " + str(list1))
print("List2: " + str(list2))

for i in range(len(list1)):
	for j in range(len(list1[i])):
		list3[i].append(list1[i][j] + list2[i][j])


print("Addition: " + str(list3))
