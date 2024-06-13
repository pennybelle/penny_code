import time
import os


def equation(x):
    failures = int(0)
    delay = 0.3
    delay_min = 0.0001
    nv_color = '\033[0;30;43m'
    color_reset = '\033[0;37;40m'
    box_color = '\033[0;30;47m'
    box = ' ' * 11
    x = int(x)
    while True:
        i = x
        while x != 1:
            if x % 2 == 0:
                x = x // 2
            else:
                x = 3 * x + 1
            print(x)
            if delay > delay_min:
                time.sleep(delay)
                delay -= 0.004
        x = i + 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
                     {box_color}{box}{color_reset}
                     {box_color} GAME OVER {color_reset}
                     {box_color}{box}{color_reset}
                     {nv_color}New Value: {color_reset}
                     {x}''')
        continue


equation(input('What number would you like to start at?\n\n'))
