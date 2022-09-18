import random

def guess(x, difficulty):
    lives = (3, 6, 9)
    if(difficulty == '1'):
        lives = lives[0]
    if(difficulty == '2'):
        lives = lives[1]
    if(difficulty == '3'):
        lives = lives[2]
    if(difficulty != '1' and difficulty != '2' and difficulty != '3'):
        return
    random_number = random.randint(1,x)
    guess = 0
    while(guess != random_number):
        if(lives <= 0):
            break
        print(f'Lives : {lives}')
        guess = int(input(f'Guess a number between 1 and {x}.\n'))
        print(f'\nChoice : {guess}')
        if(guess > random_number):
            print('Wrong!\nTry lower...\n')
            lives -= 1
        if(guess < random_number):
            print('Wrong!\nTry higher...\n')
            lives -= 1
    if(lives <= 0):
        print(f'You lose!\nThe number was {random_number}!\n')
    else:
        print('Congrats, you win!')



