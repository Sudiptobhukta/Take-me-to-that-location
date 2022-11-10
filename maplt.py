# Maplt.py- Launches a map in the browser using an address from the comand line or clipboard

# command line prompt - maply.py 'address'

import webbrowser,sys,pyperclip


if len(sys.argv) >1:
    #will check the len of the argument
    address = ' '.join(sys.argv[1:])
else:
    # will take it from the clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)