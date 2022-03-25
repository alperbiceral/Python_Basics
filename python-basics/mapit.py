import webbrowser, sys, pyperclip

# argv = ['mapit.py', 'Kelime1', 'Kelime2', 'Kelime3']
if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

# address = https://www.google/maps/search/<address>
webbrowser.open('https://www.google.com/maps/search/' + address)
