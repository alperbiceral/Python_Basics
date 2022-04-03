# added the delete part
# we are asked to add the delete part
# added part starts from line 10 to 13 
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# !!!!!!!!!!!!!!!!ADDED PART!!!!!!!!!!!!!!!!!!!!!!!!!!!!
elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
    del mcbShelf[sys.argv[2]]
# !!!!!!!!!!!!!!!!ADDED PART!!!!!!!!!!!!!!!!!!!!!!!!!!!!
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(pyperclip.paste())
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

print(mcbShelf)

mcbShelf.close()