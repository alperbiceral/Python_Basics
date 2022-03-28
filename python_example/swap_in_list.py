list = [1, 2, 3, 4, 5]

print(list)

temp = list[1]
list[1] = list[2]
list[2] = temp

print(list)
