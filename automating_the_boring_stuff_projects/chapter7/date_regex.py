# this program finds the dates in the text
import re

# find the dates
text = "Today is 04/02/2022 Saturday. Tomorrow is 05/02/2022"
regex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
matches = regex.findall(text)

# separate the day, month and year
day = []
month = []
year = []
for date in matches:
    day.append(date[0])
    month.append(date[1])
    year.append(date[2])

# check if the dates are correct
for i, j, k in zip(day, month, year):
    if int(i) < 0 or int(i) > 31 or int(j) < 0 or int(j) > 12 or int(k) < 1000 or int(k) > 2999:
        day.remove(i)
        month.remove(j)
        year.remove(k)    

if not day or not month or not year:
    print("Not have any valid date.")
else:
    for i, j, k in zip(day, month, year):
        print(i + "/" + j + "/" + k)