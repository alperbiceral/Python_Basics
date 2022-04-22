# this program looks at a certain file name pattern which is hardcoded.
# The pattern must be sorted. If it is not, make it sorted.
import os, shutil
from pathlib import Path


def main():
    target_file = Path("C:\\Users\\Alper\\Desktop")
    file_list = []
    counter = 1  # keep the sorted order with this variable

    # get the files mathced with the file name pattern and insert them into the list
    for filename in target_file.glob("spam*.txt"):
        file_list.append(filename)

    # check if the file name pattern is sorted. If not, then make them sorted.
    for filename in file_list:
        if os.path.basename(filename) != ("spam" + str(counter) + ".txt"):
            shutil.move(filename, target_file / ("spam" + str(counter) + ".txt"))
        counter += 1


if __name__ == "__main__":
    main()
