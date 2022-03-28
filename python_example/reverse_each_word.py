def reverse(word):
	return_value = ""
	for i in range(len(word)-1, -1, -1):
		return_value += word[i]
	return return_value



text = input("Enter input: ")
word_list = text.split()
result = ""

for i in range(len(word_list)):
	result += reverse(word_list[i]) + " "

print(result.strip())
