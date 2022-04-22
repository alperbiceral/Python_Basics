# this program injects the words provided by the user to the hardcoded file
import re

target_content = ""

# writes the content given in the parameter into a file and reads the file into a global variable
def read_write_file(content):
    global target_content
    # write the initial text into the file
    target_file = open("inject.txt", "w")
    target_file.write(content)
    target_file.close()

    # take the content from the file and store it in a variable
    target_file = open("inject.txt")
    target_content = target_file.read()
    target_file.close()


# substitutes the uppercase elements in the sentence with the given parameters
def substitute(adj, noun1, noun2, verb):
    global target_content
    # insert the items given by the user
    regex = re.compile(r"ADJECTIVE")
    target_content = regex.sub(f"{adj}", target_content)

    # iterate over the content to find NOUN.
    for index in range(len(target_content) - 3):
        if target_content[index : index + 4] == "NOUN":
            target_content = (
                target_content[:index] + noun1 + target_content[index + 4 :]
            )
            break

    # insert the remaining nouns
    regex = re.compile(r"NOUN")
    target_content = regex.sub(f"{noun2}", target_content)

    regex = re.compile(r"VERB")
    target_content = regex.sub(f"{verb}", target_content)


def main():
    global target_content
    # take the inputs from the user
    adj = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    noun2 = input("Enter a noun: ")

    # call the functions
    read_write_file(
        "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."
    )
    substitute(adj, noun1, noun2, verb)
    read_write_file(target_content)

    # display the result
    print(target_content)


if __name__ == "__main__":
    main()
