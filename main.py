import madlibs
import number_guesser
import rock_paper_scissors



exit = 0
while(exit == 0):
    game_choices = {1 : 'madlibs.py', 2 : 'number_guesser.py', 3 : 'rock_paper_scissors.py'}
    print(f'Games:\n')
    for x in game_choices:
        print(f'{x} : {game_choices[x]}\n')
    user_game_choice = int(input('What game would you like to play?\nSelect the game number(0 to exit) and press \'Enter\' to begin...\n'))
    if(user_game_choice == 0):
        exit = 1
    if(user_game_choice == 1):
        madlibs.start()
    if(user_game_choice == 2):
        exit = 0
        while(exit == 0):
            try:
                upper_bound = int(input('Welcome to the number guessing game!\nType an upper bound and press \'Enter\' to begin...\n'))
                number_guesser.guess(upper_bound)
                advance = input('Continue? (Y or N)').lower()
                if(advance == 'n'):
                    exit = 1
            except ValueError:
                print('Please enter an integer')
    if(user_game_choice == 3):
        advance = input('Continue? (Y or N)').lower()
        if(advance == 'n'):
            exit = 1
        