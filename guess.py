import random

lives = 7
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane', ]

secret_word = random.choice(words)
# print(secret_word) uncomment to see the secret word
clue = list('?'*5)
heart_symbol = u'\u2665'
guessed_word_corectly = False


def list_to_string(li):
    word = ''
    for i in li:
        word += i
    return word


def stats(clue):
    print(list_to_string(clue))
    print('Lives left: ' + heart_symbol * lives)


def update_clue(guessed_letter, secret_word, clue):
    # index = 0
    # while index < len(secret_word):
    #     if guessed_letter == secret_word[index]:
    #         clue[index] = guessed_letter
    #         index +=1
    for i in range(len(secret_word)):
        if guessed_letter == secret_word[i]:
            clue[i] = guessed_letter


print('Lives left: ' + heart_symbol * lives)

while lives > 0:
    guess = input('Guess a letter: ')

    if guess == secret_word:
        guessed_word_corectly = True
        break
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
        stats(clue)
        if list_to_string(clue) == secret_word:
            guessed_word_corectly = True
            break
    else:
        print('Incorrect. you lose a life')
        lives -= 1
        stats(clue)

    print('\n')

if guessed_word_corectly:
    print('you got it' + u' \u263b ' + ' won by {}/7 life'.format(lives))
else:
    print('you lost 0/7 life')
