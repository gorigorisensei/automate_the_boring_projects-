import random


print('Hi! What\'s your name?')
name = input()

answer = random.randint(0, 15)

print('Hi, ' + name +'. I\'m thinking about numbers between 0-15. ')

# write a for loop that specifies a range of guesses that a user can use

for guesses_taken in range(1,7):
    print('Take a guess!')
    user_guess = input()
    if int(user_guess) < answer:
        print('Sorry, that is too low')
    elif int(user_guess) >  answer:
        print('Sorry, that is too high')
    else:
        break

if int(user_guess) == answer:
    print('Great job, ' +  name + '. You have answered a correct number in '  +  str(guesses_taken) + ' guesses!')
else:
    print('Sorry, the correct number is ' + answer)
    
