import requests
import re
from colorama import Fore, Style

link = requests.get("https://tryhackme.com/")

regex = re.compile(r"href=\".*?\"")
matches = regex.findall(str(link.content))

for url in matches:
    url = url[6:len(url) - 1]
    try:
        if "https" in url:
            sublink = requests.get(url)
        else:
            sublink = requests.get(f"https://tryhackme.com{url}")
    except:
        print(f"{Fore.RED}[-] Cannot Connect - {sublink.url}{Style.RESET_ALL}")
        continue

    # display the status codes
    if sublink.status_code >= 100 and sublink.status_code < 200:
        print(f"{Fore.WHITE}[*] {sublink.status_code} - {sublink.url}{Style.RESET_ALL}")
    elif sublink.status_code >= 200 and sublink.status_code < 300:
        print(f"{Fore.GREEN}[+] {sublink.status_code} - {sublink.url}{Style.RESET_ALL}")
    elif sublink.status_code >= 300 and sublink.status_code < 400:
        print(f"{Fore.YELLOW}[?] {sublink.status_code} - {sublink.url}{Style.RESET_ALL}")
    elif sublink.status_code >= 400 and sublink.status_code < 500:
        print(f"{Fore.RED}[-] {sublink.status_code} - {sublink.url}{Style.RESET_ALL}")
    elif sublink.status_code >= 500 and sublink.status_code < 600:
        print(f"{Fore.MAGENTA}[!] {sublink.status_code} - {sublink.url}{Style.RESET_ALL}")
    
