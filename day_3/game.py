from random import random
num = round(random()*10)

guess = -1

while int(guess) != num:
    guess = input("Guess a number!:")
    if int(guess) != num:
        print('Try again')
print('You guessed right')