text = input("Enter input: ")
counter = {"lower":0, "upper":0}

for i in range(len(text)):
	if text[i].islower():
		counter["lower"] += 1
	elif text[i].isupper():
		counter["upper"] += 1

print("Lower: " + str(counter["lower"]))
print("Upper: " + str(counter["upper"]))
