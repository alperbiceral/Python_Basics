import time, copy, sys

conway = []
isAlive = False

# insert the initial values
for i in range(0, 6):
	conway.insert(i, ["-"]*6)

# start with the default values
conway[3][1], conway[2][3], conway[1][2], conway[3][2], conway[3][3] = "+"*5

# display function
def displayList(conway):
	for i in range(len(conway)):
		for j in range(len(conway[i])):
			print(conway[i][j], end="")
		print()

def controlList(conway):
	global isAlive
	# copying is mandatory since the list changes during the iteration
	copied = copy.deepcopy(conway)
	for row in range(len(copied)):
		for col in range(len(copied[row])):
			counter = 0

			if copied[(row-1) % len(conway)][(col-1) % len(conway[row])] == "+":
				counter += 1
			if copied[(row) % len(conway)][(col-1) % len(conway[row])] == "+":
				counter += 1
			if copied[(row+1) % len(conway)][(col-1) % len(conway[row])] == "+":
				counter += 1
			if copied[(row-1) % len(conway)][(col) % len(conway[row])] == "+":
				counter += 1
			if copied[(row+1) % len(conway)][(col) % len(conway[row])] == "+":
				counter += 1
			if copied[(row-1) % len(conway)][(col+1) % len(conway[row])] == "+":
				counter += 1
			if copied[(row) % len(conway)][(col+1) % len(conway[row])] == "+":
				counter += 1
			if copied[(row+1) % len(conway)][(col+1) % len(conway[row])] == "+":
				counter += 1

			if copied[row][col] == "+":
				if counter == 2 or counter == 3:
					isAlive = True
				else:
					isAlive = False
			elif copied[row][col] == "-":
				if counter == 3:
					isAlive = True
				else:
					isAlive = False


			if isAlive:
				conway[row][col] = "+"
			else:
				conway[row][col] = "-"



while True:
	try:
		displayList(conway)
		controlList(conway)
		print()
		time.sleep(1)
	except KeyboardInterrupt:
		sys.exit()
