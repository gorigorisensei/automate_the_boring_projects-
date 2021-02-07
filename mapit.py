#!/usr/bin/env python3

import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '870', 'tokyo']

#check if command line arguments were passed

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
   #captures after the command and turns into a string
else:
    address = pyperclip.paste()


webbrowser.open('https://www.google.com/maps/place/' + address)

