import madlibs
import number_guesser
import rock_paper_scissors

exit = 0
while(exit == 0):
    game_choices = {1 : 'madlibs.py', 2 : 'number_guesser.py', 3 : 'rock_paper_scissors.py'}
    print(f'Games:\n')
    for x in game_choices:
        print(f'{x} : {game_choices[x]}\n')
    user_game_choice = input('What game would you like to play?\nSelect the game number(0 to exit) and press \'Enter\' to begin...\n')
    if(user_game_choice == '1' or user_game_choice == '2' or user_game_choice == '3' or user_game_choice == '0'):
        if(user_game_choice == '0'):
            exit = 1
        if(user_game_choice == '1'):
            madlibs.start()
            advance = input('Continue? (Y or N)').lower()
            if(advance == 'n'):
                exit = 1
        if(user_game_choice == '2'):
            print('Welcome to Number Guessor!\n')
            ng_exit = 0
            while(ng_exit == 0):
                    user_difficulty = input('Enter difficulty...\n(\'1\', \'2\', \'3\'):\n')
                    if(user_difficulty == '1' or user_difficulty == '2' or user_difficulty == '3' or user_difficulty == '0'):
                        upper_bound = input('Type an upper bound and press \'Enter\' to begin...\n')
                        try:
                            upper_bound = int(upper_bound)
                            number_guesser.guess(upper_bound, user_difficulty)
                            advance = input('Play again? (Y or N)').lower()
                            if(advance == 'n'):
                                ng_exit = 1
                        except ValueError:
                            print('Enter an integer value for the upper bound...')
                    else:
                        print('Choose a difficulty between 1 and 3...')
        if(user_game_choice == '3'):
            advance = input('Continue? (Y or N)').lower()
            if(advance == 'n'):
                exit = 1
    else:
        print('Choose from the given options...')
        