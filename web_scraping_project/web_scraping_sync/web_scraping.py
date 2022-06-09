import requests
import re
import sys
import colorama
from colorama import Fore, Style

url_file = open("url_list", "w")
try:
    weekly = True
    date = sys.argv[1]
except:
    weekly = False

def get_full_content(): # default değer
    global url_file
    try:
        if weekly:
            # get the date as the argument so that user can view which date they want to view
            # format of the date: YYYY-MM-DD/YYYY-MM-DD
            # first date and the second date differ at most 7 days
            urls = requests.get(f"http://www.tweettioc.com/v1/tweets/{date}/url")
            url_file.write(str(urls.content))
            url_file.close()
        else:
            # get the content from the url into a file
            urls = requests.get("http://www.tweettioc.com/feed/daily/url")
            url_file.write(str(urls.content))
            url_file.close()

        print(f"{Fore.GREEN}[+] Successfuly got the data{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}[-] Unsuccessful to get the data{Style.RESET_ALL}")
        sys.exit()

def get_regex():
    global url_file
    try:
        # read the file content into a variable
        with open("url_list", "r") as url_file:
            content = url_file.read()
            print(f"{Fore.GREEN}[+] Successfuly read the file{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}[-] Unsuccessfuly read the file{Style.RESET_ALL}")

    if weekly:
        try:
            # look for the anonfiles urls
            regex = re.compile(r"https://anonfiles\..*?\"")
            match = regex.findall(content)
            # append the file with the found anonfiles urls
            with open("anonfiles_7day.txt", "w") as anon_file:
                for url in match:
                    url = url[: len(url) - 1]
                    anon_file.write(url + "\n")
            print(f"{Fore.GREEN}[+] Successfuly written anonfiles data{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}[-] Unable to write anonfiles data{Style.RESET_ALL}")

        try:
            # look for the pastebin urls
            regex = re.compile(r"(https://pastebin\..*?\")")
            match = regex.findall(content)
            # append the file with the found pastebin urls
            with open("pastebin_7day.txt", "w") as pastebin_file:
                for url in match:
                    url = url[: len(url) - 1]
                    pastebin_file.write(url + "\n")
            print(f"{Fore.GREEN}[+] Successfuly written pastebin data{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}[-] Unable to write pastebin data{Style.RESET_ALL}")
    else:
        try:
            # get the pastebin urls from the content
            regex = re.compile(r"https://pastebin\..*?http")
            match = regex.findall(content)
            # write the new pastebin url to the file
            url_file = open("pastebin_daily.txt", "w")
            for url in match:
                url = url[: len(url) - 6]
                url_file.write(url + "\n")
            print(f"{Fore.GREEN}[+] Successfuly written pastebin data{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}[-] Unable to write pastebin data{Style.RESET_ALL}")

        try:
            # get the anonfiles urls from the content
            regex = re.compile(r"https://anonfiles\..*?http")
            match = regex.findall(content)
            # write the new anonfiles url to the file
            url_file = open("anonfiles_daily.txt", "w")
            for url in match:
                url = url[: len(url) - 6]
                url_file.write(url + "\n")
            print(f"{Fore.GREEN}[+] Successfuly written anonfiles data{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}[-] Unable to write anonfiles data{Style.RESET_ALL}")

def main():
    get_full_content()
    get_regex()
    
    print(f"{Fore.GREEN}[+] Program ended{Style.RESET_ALL}")
    sys.exit()

if __name__ == "__main__":
    main()
