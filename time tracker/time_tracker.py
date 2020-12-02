from os import system
import time


def save(name, time):
    with open('report.log', 'a') as file:
        file.write(name+'-'+time+'\n')


def report():
    with open('report.log') as file:
        print(file.read())


def time_convert(sec):
    mins = sec // 60
    hrs = mins // 60
    mins = mins % 60
    sec = sec % 60
    return '{}:{}:{}'.format(int(hrs), int(mins), int(sec))


def stopwatch():
    input('press enter to start stopwatch')
    start_time = time.time()
    input('press enter again to stop stopwatch')
    end_time = time.time()
    return time_convert(end_time - start_time)


user = input('(q) to start record or (r) to show report :').lower()
print('')
if user == 'r':
    report()

elif user == 'q':
    name = input('enter the subject: ')
    if name:
        time_lapsed = stopwatch()
        print(time_lapsed)
        save(name, time_lapsed)
    else:
        print('subject can\'t be empty')
