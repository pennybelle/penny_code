import random
import os


def clear(): os.system('cls')


color = ""
cr = "\033[0;37;40m"
divider = " - "
while True:
    x = int(1)
    y = int(random.uniform(1, 100))
    while x >= y:
        x += y
        color = "\033[1;31;40m  "
        break
    while x < y:
        x -= y
        color = "\033[0;37;42m  "
        break
    print(color + cr + divider + str(y))
    clear()
    continue
