import os
import sys
import time
import json
from readchar import readkey

with open("data.json","r") as file_content:
   data = json.load(file_content)

blue = data["default settings"]["colors"]["blue"].encode("utf-8").decode("unicode_escape")
cyan = data["default settings"]["colors"]["cyan"].encode("utf-8").decode("unicode_escape")
green = data["default settings"]["colors"]["green"].encode("utf-8").decode("unicode_escape")
magenta = data["default settings"]["colors"]["magenta"].encode("utf-8").decode("unicode_escape")
red = data["default settings"]["colors"]["red"].encode("utf-8").decode("unicode_escape")
yellow = data["default settings"]["colors"]["yellow"].encode("utf-8").decode("unicode_escape")
black = data["default settings"]["colors"]["black"].encode("utf-8").decode("unicode_escape")
bright_black = data["default settings"]["colors"]["bright_black"].encode("utf-8").decode("unicode_escape")
white = data["default settings"]["colors"]["white"].encode("utf-8").decode("unicode_escape")
up = "w"
down = "s"
right = "a"
left = "d"
selColor = blue


def menu():
    clear()
    option = 1
    while True:
        if option == 1:
            clear()
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
                print(white + "")
                clear()
                break


def clear():
    time.sleep(0.01)
    os.system('cls')


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


def menu_options_Selcolor(): # not implemented, but can work ¯\_(ツ)_/¯ 
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


def write(message, delay=.01): # not implemented either
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)
    print('')


menu()
