import random


print('Welcome to guess the number')
guess = int(input('Please enter a number between 1 and 20: '))
number = random.randrange(1,21)
guesses = 1

while guess != number:
    if guess > 20:
        guess = int(input('Number not in range of 1-20, please enter a number between 1 and 20: '))
        guesses += 1
    elif guess > number:
        guess = int(input('Number too high, please enter a number between 1 and 20: '))
        guesses += 1
    elif guess < number:
        guess = int(input('Number too low, please enter a number between 1 and 20: '))
        guesses += 1
print('Correct my number was', number, 'and you guessed my number in', guesses, 'guesses')



    


