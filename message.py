
import pprint
message = 'It was a bright cold day in April, and poop was flying everywhere.'
count = {}

for character in message.upper():
    count.setdefault(character, 0) #character has only one letter value 
    count[character] = count[character] + 1

pprint.pprint(count)
