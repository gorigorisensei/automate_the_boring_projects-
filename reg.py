import re

message = "Hi! this is a randome message. Your phone number is 111-222-1111, 111-222-3412"

phone_regex = re.compile(r'(?i)(cat|your|message)')
matched_object = phone_regex.findall(message)
print(matched_object)

#write a regular expression code that has phone number 222-222-1111
#match only the first 3 digits using search & group methods


#exercise2 : create a regular expression rule that matches either cat, your, or message
#find all of those instances and put them on a list
