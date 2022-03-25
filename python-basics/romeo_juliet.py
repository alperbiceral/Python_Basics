# just write the url content to the indicated file
import requests

content = requests.get('https://automatetheboringstuff.com/files/rj.txt')

with open('romeo_juliet.txt', 'w') as destFile:
	destFile.write(content.text)

destFile.close()
