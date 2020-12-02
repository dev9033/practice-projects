import random
import string

# you can add more adjectives
adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange',
              'yellow', 'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']

# you can add more noun
nouns = ['apple', 'dinosaur', 'ball', 'toaster',
         'goat', 'dragon', 'hammer', 'duck', 'panda']

print("welcome to password picker")

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randint(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print('your password: {}'.format(password))

    response = input("like this one? type 'y' or 'n': ")
    if response == 'y':
        break
