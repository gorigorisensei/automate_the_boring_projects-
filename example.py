import random

print('Hi What\'s your name?')
name = input()
print('Hello, ' + name +  '! I\'m thinking of a number between 1-15.')

correct_answer = random.randint(1,15)

for guessesTaken in range(1,7):
    print('Can you guess?')
    user_guess = input()
    if int(user_guess) > correct_answer:
        print('Sorry, too high.')
    elif int(user_guess) < correct_answer:
        print('Sorry, too low')
    else:
        break

if correct_answer == int(user_guess):
    print('Great job, ' + name + '! You have guessed the correct number in ' + str(guessesTaken) + ' times!')
else:
    print('Sorry, the correct answer was ' + str(correct_answer))

    
    
