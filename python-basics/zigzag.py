import time, sys
line = "********"
spaces = " "

while True:
	try:
		for i in range(5):
			time.sleep(0.2)
			print(spaces * i + line)

		for i in range(4, -1, -1):
			time.sleep(0.2)
			print(spaces * i + line)
	except KeyboardInterrupt:
		sys.exit()
