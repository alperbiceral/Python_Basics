# this program checks if the password is strong
# strong password is at least 8 characters long, contains at least one lowercase and one uppercase and one digit
# implement the program with regular expressions to practice
import re, sys

password = "Password123"

# check if password contains a digit at least one
regex = re.compile(r"\d+")
match = regex.search(password)

if match == None:
    print("Password is not strong enough.")
    sys.exit()

# check if password contains a alpha numeric character at least one
regex = re.compile(r"\w+")
match = regex.search(password)

if not match:
    print("Password is not strong enough.")
    sys.exit()

# check if password contains both uppercase and lowercase characters at least one
is_lower = False
is_upper = False
for ch in match.group():
    if ch.islower():
        is_lower = True
    elif ch.isupper():
        is_upper = True

if not is_lower or not is_upper:
    print("Password is not strong enough.")
    sys.exit()

print("Password is strong.")