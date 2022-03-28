string1 = "claß"
string2 = "class"

print(string1)
print(string2)

if string1.casefold() == string2.casefold():
	print("SAME")
else:
	print("DIFFERENT")
