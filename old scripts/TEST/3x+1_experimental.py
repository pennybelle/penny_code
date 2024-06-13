
import logging
import os
# import sys
import time
# import colorama
# from colorama import init, Fore, Back, Style
# init(convert=True)
def clear(): os.system('cls')
# from rich.panel import Panel
# from rich.table import Table
# from rich.console import Console

# console = Console()
# table = Table()

# table.add_column("Total Failures: " + str(f))
# table.add_column("Current number: " + str(y))
# table.add_column(log)

# panel = Panel.fit(
#     table,
#     title="3x+1",
#     border_style="yellow",
#     title_align="center",
#     padding=(1, 2),
# )


y = int(pow(2, 68))
c = int(0)
f = int(0)


logger = logging.getLogger('3x+1')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
fh = logging.FileHandler('3x+1.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
log = ""
new_value = ""
line = "\n---------------------\n"
game_start = str("\n----------\nGAME START\n----------\n")
game_over = str("\n---------\nGAME OVER\n---------\n")
start = False

print("Welcome to 3x+1!\n")
time.sleep(3)
print("Here are the rules:\n")
time.sleep(2)
print("You enter a number at the prompt. If that number is Odd,")
time.sleep(3)
print("it will be multiplied by 3 and then added to 1.")
time.sleep(3)
print("If it is Even however, it will be divided by 2.\n")
time.sleep(3)
print("If your number reaches 1, then its:" + "\n" * 3 + str(game_over) + "\n" * 3)
time.sleep(5)

while not start:
    start_input = input("Would you like to begin? (y/n)\n\n")
    if start_input == "n":
        quit()
    elif start_input == "y":
        start = True
        break
    elif start_input != "y" or "n":
        clear()
        print("\n\nInvalid Input, please try again")
        continue

logger.info(game_start)

while start:
    clear()
    time.sleep(1)
    num = input("What number would you like to start with?\n\n")
    if num != "max":
        y = int(num)
    else:
        y = int(y)
    start = False
    break

print("\n\n")

while True:
    clear()
    # console.print(panel)
    x = int(y + 1)
    new_value = str("NEW VALUE - " + str(int(x)) + "\n")
    print(new_value)
    logger.info(new_value)
    while x != 1:
        if int(x % 2) != 0:
            c += int(1)
            i = int(x)
            x = int(3 * x + 1)
            log = str("UP   - " + str(c) + " - " + str(int(x)))
            print(log)
            logger.info(log)
            continue
        elif int(x % 2) == 0:
            c += int(1)
            i = int(x)
            x /= int(2)
            log = str("DOWN - " + str(c) + " - " + str(int(x)))
            print(log)
            logger.info(log)
            continue
    while x == 1:
        f += int(1)
        y += int(1)
        c = int(0)
        game_over = str(line + "GAME OVER - Failures: " + str(f) + line)
        print(game_over)
        logger.info(game_over)
        break
    continue
