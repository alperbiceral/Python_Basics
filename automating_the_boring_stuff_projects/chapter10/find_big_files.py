# this file looks for the files in the target folder if their size exceeds 20KB
import os
from pathlib import Path

file_list = []
target_file = Path("C:\\Users\\Alper\\Desktop\\yazılar")

for current, subfolders, subfiles in os.walk(target_file):
    for subfile in subfiles:
        # check if the file size is above 20KB 
        if os.path.getsize(target_file / current / subfile) > 20000:
            file_list.append(subfile)

print(file_list)