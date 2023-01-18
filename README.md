# menu-demo

This is a demo. It uses packages like `readkey`, `os`, `sys`, and `time`. `codes.py` is the file for storing all the escape codes.


When you run the code, you will first get an output like this:

```
MENU:
-> Start
   Options
   Quit
```

## Navigation:

| Key | Function |
| ----------- | ----------- |
| z | selection button |
| x | back button |
| up arrow key | moves selector up |
| down arrow key | moves selector down |

### How it works:

Its very simple. `a = readkey()` is searching for any input from the keyboard. When input recieved, we use if-statements to check what key if pressed. The output is determined on what `option = 1` is. By default, `option` is 1. We change the option efficiently by using the code down below:

```
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
```

Depending on what option is, we print a certain output to the terminal:

```
if option == 1:
    print('')
elif option == 2:
    print('')
...
```
We also have the when the `x` and `z` key are pressed. We have `x` set as the back button and `z` as the selection button.

```
if a == 'z':
    if option == 1:
        start()
    if option == 2:
        menu_Options()
    if option == 3:
        break
elif a == 'x':
    break
```

