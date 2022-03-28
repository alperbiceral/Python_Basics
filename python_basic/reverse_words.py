text = input("Enter input: ")
word_list = text.split()
result = ""

for i in range(len(word_list)-1, -1, -1):
	result += word_list[i] + " "

print(result)
