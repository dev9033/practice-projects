from random import randint

while True:
    usr_inp = input('Roll the dice? (y/n): ')
    if usr_inp == 'n':
        break
    elif usr_inp == 'y':
        print(randint(1,6))
    else:
        print('invalid choice, try again')