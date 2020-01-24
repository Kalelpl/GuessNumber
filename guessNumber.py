import random

a = random.randint(0, 8)
guess = 0
attempt = 0
print ('Hi! Try to guess a number between 0-8')


while a != guess:
    number = int(input())
    attempt = attempt + 1
    if number < a:
        print('The number you are looking for is higher')
    elif number > a:
        print('The number you are looking for is lower')
    else:
        print('You are correct! '+ str(a) + ' was the number I was looking for. It took you ' + str(attempt) + ' attempts')
        break
