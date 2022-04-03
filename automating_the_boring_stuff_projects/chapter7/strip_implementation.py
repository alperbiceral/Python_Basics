# remove whitespaces from the beginning and from the end of the string, if there is not any argument given
# remove the character, if the argument given (choose the argument's first character)
import re, sys

# sample text
text = "   Python  rocks       "

# if any argument is not given
if len(sys.argv) == 1:
    regex = re.compile(r"^\s+|\s+$")
    stripped = regex.sub(r"", text)
# if there is at least one argument (no matter how long it is or how many argument we have, we just take the first character)
elif len(sys.argv) >= 2:
    regex = re.compile(f"{sys.argv[1][0]}")
    stripped = regex.sub(r"", text)

# display the results
print(stripped)
print("The number of characters: ", len(stripped))