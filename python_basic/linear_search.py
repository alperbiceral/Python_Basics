import sys

list = [5, 9, 6, 7, 3]

while True:
	try:
		searching = int(input("Search for the number: "))
		break
	except ValueError:
		print("Invalid input")

for i in range(len(list)):
	if searching == list[i]:
		print("Found at the index " + str(i))
		sys.exit()

print(str(searching) + " does not exist.")
