from random import randint
print("""
 _  __    __    _  __ _        __ __ __   ___ __       _  _  __
|_)|_ |V||_ |V||_)|_ |_)   |  |_ (_ (_     | (_    |V|/ \|_)|_
| \|__| ||__| ||_)|__| \   |__|____)__)   _|___)   | |\_/| \|__

""")


def user_in():
    return int(input())


def hint(cmp, usr):
    if cmp > usr:
        print('give a litte more')
    elif usr > cmp:
        print('give a little less')


# choosing level
levels = {1: 10, 2: 50, 3: 100}
print('choose your level (1) low  (2) medium (3) hard: ', end='')
usr_level = user_in()
while usr_level not in levels:
    print('{} is an invalid option choose again: '.format(usr_level, end=''))
    usr_level = user_in()
usr_level = levels[usr_level]

# game logic
cmp_choice = randint(0, usr_level)
print('choose a number from 0 to {}'.format(usr_level))
usr_choice = user_in()
steps = 0
while cmp_choice is not usr_choice:
    hint(cmp_choice, usr_choice)
    steps += 1
    usr_choice = user_in()
print('your score is -{}'.format(steps))
