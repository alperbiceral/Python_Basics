# this program injects the words provided by the user to the hardcoded file
import re

# take the inputs from the user
adj = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb = input("Enter a verb: ")
noun2 = input("Enter a noun: ")

# write the initial text into the file
target_file = open("inject.txt", "w")
target_file.write("The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.")
target_file.close()

# take the content from the file and store it in a variable
target_file = open("inject.txt")
target_content = target_file.read()
target_file.close()

# insert the items given by the user
regex = re.compile(r"ADJECTIVE")
target_content = regex.sub(f"{adj}", target_content)

# iterate over the content to find NOUN.
for index in range(len(target_content) - 3):
    if target_content[index:index + 4] == "NOUN":
        target_content = target_content[:index] + noun1 + target_content[index + 4:]
        break

# insert the remaining nouns
regex = re.compile(r"NOUN")
target_content = regex.sub(f"{noun2}", target_content)

regex = re.compile(r"VERB")
target_content = regex.sub(f"{verb}", target_content)

# save the last result to the file and take the content from the file and display it
target_file = open("inject.txt", "w")
target_file.write(target_content)
target_file.close()

target_file = open("inject.txt")
target_content = target_file.read()
target_file.close()
print(target_content)