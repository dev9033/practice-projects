from random import randint


def take_input():
    user_in = int(input('choose a number: '))
    return user_in


cnt = 0
random_number = randint(0, 100)
num = take_input()

while random_number is not num:
    if num <= random_number:
        print("try greater number")
    elif num >= random_number:
        print("try lesser number")
    cnt += 1
    num = take_input()
print('you won on', cnt, 'steps')
