import random

def guess(x):
        lives = 3
        random_number = random.randint(1,x)
        guess = 0
        while(guess != random_number):
            if(lives <= 0):
                print('You lose!')
                break
            print(f'Lives : {lives}')
            guess = int(input(f'Guess a number between 1 and {x}.\n'))
            print(f'\nChoice : {guess}')
            if(guess > random_number):
                lives -= 1
                print('Wrong!\nTry lower...\n')
            if(guess < random_number):
                lives -= 1
                print('Wrong!\nTry higher...\n')
        if(lives > 0):
            print('Congrats, you win!')



