import random

print('Hi! What\'s your name?')

name = input()

print('Hello, ' + name + '! I\'m thinking of a number between 1 and 15.')

answer = random.randint(1,15)

for guessesTaken in range(1,7):
    print('Take a guess!') 
    user_guess = input()
    if int(user_guess) < answer:
        print('Sorry, it\'s too low')
    elif int(user_guess) > answer:
        print('Sorry, it\'s too high')
    else:
        break

if int(user_guess) == answer:
    print('Great job, ' + name + '! You\'ve guessed a correct number within ' + str(guessesTaken) + ' times!')
else:
    print('Sorry, the correct number is ' + str(answer) + '.')
