import re, pprint
# TODO: Copy the text into a variable
message = """
"""

# TODO: extract the phone numbers
# xxx-xxx-xxxx	(xxx) xxx-xxxx
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d)')

# TODO: extract the emails
# xxx@xxx.com | xxx@xxx.net
emailRegex = re.compile(r'(\w+@\w+\.(com|net))')

phoneList = phoneRegex.findall(message)
emailList = emailRegex.findall(message)

for i in range(len(phoneList)):
	pprint.pprint(phoneList[i][0])

for i in range(len(emailList)):
	pprint.pprint(emailList[i][0])
