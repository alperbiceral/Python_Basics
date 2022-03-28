# the first two are the same but the last one is different
list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6]
list3 = [1, 2, 3, 4, 5, 7]

print(list1)
print(list2)
print(list3)

print("\nList1 and List2 are the same: " + str(list1 == list2))
print("List1 and List3 are the same: " + str(list1 == list3))
print("List3 and List2 are the same: " + str(list3 == list2))
