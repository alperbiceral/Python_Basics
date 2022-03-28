list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [1, 2, 3]

print("List1: " + str(list1))
print("List2: " + str(list2))
print(list(set(list1) - set(list2)))
