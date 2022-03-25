# raise an exception if the symbol is more than one character
def printBox(symbol, width, height):
	if len(symbol) != 1:
		raise Exception("'symbol' must have the height of 1")

	print(symbol * width)
	for i in range(height - 2):
		print(symbol + (' ')*(width-2) + symbol)

	print(symbol * width)

printBox('**', 15, 5)
