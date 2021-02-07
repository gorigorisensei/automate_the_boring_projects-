#!/usr/bin/env

import re, pyperclip


#TODO: create a regex for phone numbers
email_and_phone_regex = re.compile(r'(?s)(\S+@\S+[A-Za-z]\s*[\d-]{10,})')

# get the text off the clipboard
text = pyperclip.paste()
#Extract the email/ phone from this text
email_and_phone_found =email_and_phone_regex.findall(text)



#copy the extracted email/phone to the clipboard

results = '|\n'.join(email_and_phone_found)

pyperclip.copy(results)

#join method finds transforms iterable objects into a string
