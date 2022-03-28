import sys

list1 = [1, 2, 3, 4]
copied_list = []
argument_copy = []

print("List1: " + str(list1))
print("Copied_list: " + str(copied_list))
print("Argument_copy: " + str(argument_copy))

for i in range(len(list1)):
	copied_list.append(list1[i])

for i in range(1, len(sys.argv)):
	argument_copy.append(sys.argv[i])

print()
print("List1: " + str(list1))
print("Copied_list: " + str(copied_list))
print("Argument_copy: " + str(argument_copy))
