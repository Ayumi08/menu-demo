import os
import sys
import time
from codes import *
from readchar import readkey


selColor = blue


def menu():
    clear()
    option = 1
    while True:
        if option == 1:
            clear()  # clears the last output
            print(white + 'MENU:')
            print(selColor + '-> Start')
            print(white + '   Options')
            print(white + '   Quit')

        if option == 2:
            clear()
            print(white + 'MENU:')
            print(white + '   Start')
            print(selColor + '-> Options')
            print(white + '   Quit')

        if option == 3:
            clear()
            print(white + 'MENU:')
            print(white + '   Start')
            print(white + '   Options')
            print(selColor + '-> Quit')

        a = readkey()
        if a == down:
            if option < 3:
                option += 1
            else:
                option = 1
        elif a == up:
            if option > 1:
                option -= 1
            else:
                option = 3

        else:
            clear()

        if a == 'z':
            if option == 1:
                start()
            if option == 2:
                menu_Options()
            if option == 3:
                break


def clear():
    time.sleep(0.01)
    os.system('clear')


def start():
    clear()
    option = 1
    while True:
        if option == 1:
            print('there is no start right now.')

        a = readkey()

        if a == 'x':
            clear()
            break
        else:
            clear()


def menu_Options():
    clear()
    option = 1
    while True:
        if option == 1:
            print(white + 'OPTIONS:')

        a = readkey()

        if a == 'x':
            clear()
            break
        elif a == 'z':
            if option == 1:
                clear()
                break
        else:
            clear()


def menu_options_Selcolor():
    clear()
    option = 1
    while True:
        if option == 1:
            print(white + 'SELECTION COLOR:')
            print(selColor + '-> Blue')
            print(white + '   Cyan')
            print(white + '   Green')
            print(white + '   Magenta')
            print(white + '   Red')
            print(white + '   Yellow')

        elif option == 2:
            print(white + 'SELECTION COLOR:')
            print(white + '   Blue')
            print(selColor + '-> Cyan')
            print(white + '   Green')
            print(white + '   Magenta')
            print(white + '   Red')
            print(white + '   Yellow')
        elif option == 3:
            print(white + 'SELECTION COLOR:')
            print(white + '   Blue')
            print(white + '   Cyan')
            print(selColor + '-> Green')
            print(white + '   Magenta')
            print(white + '   Red')
            print(white + '   Yellow')
        elif option == 4:
            print(white + 'SELECTION COLOR:')
            print(white + '   Blue')
            print(white + '   Cyan')
            print(white + '   Green')
            print(selColor + '-> Magenta')
            print(white + '   Red')
            print(white + '   Yellow')
        elif option == 5:
            print(white + 'SELECTION COLOR:')
            print(white + '   Blue')
            print(white + '   Cyan')
            print(white + '   Green')
            print(white + '   Magenta')
            print(selColor + '-> Red')
            print(white + '   Yellow')
        elif option == 6:
            print(white + 'SELECTION COLOR:')
            print(white + '   Blue')
            print(white + '   Cyan')
            print(white + '   Green')
            print(white + '   Magenta')
            print(white + '   Red')
            print(selColor + '-> Yellow')

        a = readkey()

        if a == 'x':
            clear()
            break
        elif a == 'z':
            if option == 1:
                selColor = blue
            elif option == 2:
                selColor = cyan
            elif option == 3:
                selColor = green
            elif option == 4:
                selColor = magenta
            elif option == 5:
                selColor = red
            elif option == 6:
                selColor = yellow

        if a == down:
            if option < 6:
                option += 1
            else:
                option = 1
        elif a == up:
            if option > 1:
                option -= 1
            else:
                option = 6


def write(message, delay=.01):
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)
    print('')


menu()
