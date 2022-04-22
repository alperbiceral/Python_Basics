import requests
import sys
import re
from colorama import Fore, Style

# go to the target web address
argument = sys.argv[1]
parameter = {"q":argument}
search_result = requests.get("https://imgur.com/search", params=parameter)

# look for how many posts are there
regex = re.compile(r"class=\"post\"")
matches = regex.findall(str(search_result.content))
print("Number of the first set of images: " + str(len(matches)))

# search for the first image
regex = re.compile(r"//i\.imgur\.com/.*?\.jpg")
matches = regex.search(str(search_result.content))
first_image_url = "https:" + str(matches.group())

# write the first image to a file
first_image = requests.get(first_image_url)
try:
    with open("first_image.jpg", "wb") as image_file:
        image_file.write(first_image.content)
    print(f"{Fore.GREEN}[+] Downloaded successfuly{Style.RESET_ALL}")
except:
    print(f"{Fore.RED}[-] Unable to download{Style.RESET_ALL}")

sys.exit()