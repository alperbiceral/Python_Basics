is_duplicate = False
positive = [1, 2, 3, 3, 4, 5, 6]
negative = [1, 2, 3, 4, 5, 6, 7]

print("List1: " + str(positive))
print("List2: " + str(negative) + "\n")

for i in range(len(positive)):
	for j in range(i + 1, len(positive)):
		if positive[i] == positive[j]:
			is_duplicate = True
			print("DUPLICATE: " + str(positive[i]))
			positive.remove(positive[j])
			positive.remove(positive[i])
			break
if not is_duplicate:
	print("ALL UNIQUE")

is_duplicate = False
for i in range(len(negative)):
	for j in range(i + 1, len(negative)):
		if negative[i] == negative[j]:
			is_duplicate = True
			print("DUPLICATE: " + str(negative[i]))
			positive.remove(negative[j])
			positive.remove(negative[i])
			break
if not is_duplicate:
	print("ALL UNIQUE")

print("\nREMOVED DUPLICATES:")
print("List1: " + str(positive))
print("List2: " + str(negative) + "\n")
