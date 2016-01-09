__author__ = 'Călin Sălăgean'

from lib.backtrack import Backtrack


while True:
    command = input('Type exit or press enter to continue: ')

    if command == 'exit':
        break

    list = []

    while True:
        elem = input('Integer or float: ')
        try:
            int(elem)
            float(elem)

            list.append(elem)
        except:
            print('Continue!')
            break

    if len(list):
        backtrack = Backtrack(list)
        backtrack.determine()
        print(backtrack.result)
    else:
        print('One element required')