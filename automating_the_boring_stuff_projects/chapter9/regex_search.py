# this program scans all .txt files in the cwd and looks if they have the searching pattern.
import re
from pathlib import Path

# get the list of the .txt files in the current working directory
path = Path.cwd()
text_files = path.glob("*.txt")
list_of_files = list(text_files)

# look at the content of the found files and search for a specific regex
matches = []
for elem in list_of_files:
    # open the files in the file list
    text_file = open(elem)
    file_content = text_file.readline()

    # search for the regex 555-555-5555
    regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
    matches.append(regex.findall(file_content))

# remove the empty list items
for num in matches:
    if num == []:
        matches.remove(num)

# print the list items
for num in matches:
    print(num)