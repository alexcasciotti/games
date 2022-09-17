import number_guesser

# number guesser application
exit = 0
while(exit == 0):
    try:    
        upper_bound = int(input('You get 3 lives...\nEnter an upper bound: '))
        number_guesser.guess(upper_bound)
        exit = 1
    except ValueError:
        print('The upper bound must be an integer.')