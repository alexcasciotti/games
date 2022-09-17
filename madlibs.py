import random
#Madlibs is a game where the player completes a story by replacing missing words with their own unique choices.

story_bank = ['The (noun) is (adjective)! What a wonderful (noun)!']
story = random.choice(story_bank)

def start():
    print(f'\nWelcome to madlibs!\nHere is your story...\n{story}')
    print(build_story())

def build_story():
    new_story = ''
    index = 0
    while(index < len(story)):
        if(story[index] == '('):
            pos = ''
            while(story[index] != ')'):
                pos += story[index]
                index += 1
            pos += story[index]
            index += 1
            missing_word = input(f'Enter a {pos}...\n').upper()
            for x in missing_word:
                new_story += x
        new_story += story[index]
        index += 1     
    return new_story
start()