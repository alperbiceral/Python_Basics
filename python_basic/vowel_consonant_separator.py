str1 = input("Enter input: ")
vowels = []
consonants = []

for i in range(len(str1)):
	if str1[i].lower() == "a" or str1[i].lower() == "e" or str1[i].lower() == "i" or str1[i].lower() == "o" or str1[i].lower() == "u":
		vowels.append(str1[i])
	elif str1[i].isalpha():
		consonants.append(str1[i])

print(vowels)
print(consonants)

print("Number of vowels: " + str(len(vowels)))
print("Number of consonants: " + str(len(consonants)))
