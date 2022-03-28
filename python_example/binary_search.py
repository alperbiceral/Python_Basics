list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
	try:
		searching = int(input("Search: "))
		break
	except ValueError:
		print("Invalid input")

def binary_search(first, last):
	mid = int((first + last) / 2)

	if first > last:
		print(str(searching) + " does not exist")
		return False

	if list[mid] == searching:
		print("Found at the index: " + str(mid))
		return True
	elif list[mid] > searching:
		last = mid - 1
		binary_search(first, last)
	else:
		first = mid + 1
		binary_search(first, last)

binary_search(0, len(list) - 1)
