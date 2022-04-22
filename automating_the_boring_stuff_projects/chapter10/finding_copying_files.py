# this program copies the text files in the Desktop and pastes them into another folder
import os, shutil
from pathlib import Path


def main():
    file_list = []
    target_path = Path("C:\\Users\\Alper\\Desktop")

    # get the txt files
    for filename in list(target_path.glob("*.txt")):
        file_list.append(filename)

    # copy the files into another location
    for filename in file_list:
        shutil.copy(filename, target_path / "Python_Part2_examples")


if __name__ == "__main__":
    main()
