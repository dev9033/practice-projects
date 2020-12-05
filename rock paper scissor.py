from random import randint


def game(u, com):
    user_score = False
    com_score = False
    if u == 1 and com == 3:
        user_score = True
    elif u == 2 and com == 1:
        user_score = True
    elif u == 3 and com == 2:
        user_score = True
    elif (u == 1 and com == 1) or (u == 2 and com == 2) or (u == 3 and com == 3):
        return 'nobody'
    else:
        com_score = True

    if user_score:
        return 'u'
    else:
        return 'com'

user_score = 0
com_score = 0
while True:
    while True:
        u = int(input('1: rock\n2: paper\n3: scissors\npick a number\n>>> '))
        if 1 <= u <= 3:
            break
        else:
            print('try again')
    com = randint(1, 3)
    
    play = game(u,com)
    print(f'{play} won')
    if play == 'u':
        user_score += 1
    elif play == 'com':
        com_score += 1

    rematch = str(input('wanna play again? (↵/n)\n>>> '))
    if rematch == 'n' or rematch == 'N':
        print(f"scores:\nur's {user_score}\ncom's {com_score}")
        break