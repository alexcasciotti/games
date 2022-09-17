import random
#Madlibs is a game where the player completes a story by replacing missing words with their own unique choices.

story_bank = ['The (noun) is (adjective)! What a wonderful (noun)!', 'Today I went to the zoo. I saw a\
___________(adjective)\
_____________(Noun) jumping up and down in its tree. \
He _____________(verb, past tense) __________(adverb) \
through the large tunnel that led to its _______(adjective) \
__________(noun). I got some peanuts and passed \
them through the cage to a gigantic gray _______(noun) \
towering above my head. Feeding that animal made\
me hungry. I went to get a __________(adjective) scoop \
of ice cream. It filled my stomach. Afterwards I had to \
__________(verb) __________ (adverb) to catch our bus. \
When I got home I __________(verb, past tense) my \
mom for a __________(adjective) day at the zoo.']
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