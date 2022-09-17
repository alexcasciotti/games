#Madlibs is a game where the player completes a story by replacing missing words with their own unique choices.

def build_story():
    print('\nWelcome to madlibs!\nHere is your story...\nThe sky is (adjective)! What a wonderful (noun)!\n')
    adj1 = input("Enter an adjective: ")
    noun1 = input("Enter an noun: ")    
    return f'\nThe sky is {adj1}! What a wonderful {noun1}!\n'
    