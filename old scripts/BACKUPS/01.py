import os
def clear(): os.system('cls')


x = 1
while True:
    clear()
    while x == 0:
        x += 1
        print(x)
    clear()
    while x != 0:
        x -= 1
        print(x)