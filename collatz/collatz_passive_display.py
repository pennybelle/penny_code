import time
from os import system, path, name

log = 'HighScore.log'

# TODO: create clicker game where x += 1 when the user clicks sequence would splice
# together to create the ability to control your score if you never stop clicking.

def file_check():
    if path.exists(log): return True
    else: return False

def clear(): system('cls' if name == 'nt' else 'clear')

def start():
    if not file_check():
        record = open(log, 'w+')
        record.writelines(['Best Seed: 0\nHighscore: 0'])
        record.close()

    # set terminal size
    size = 'mode 54,50'
    system(size)

def game(x):
    current_score = int(0)  # ingame highscore, starts at 0 unless highscore is greater
    record = open(log, 'r')
    highscore = int(record.readlines()[1][10:])  # highscore in log file (2nd line)
    steps = int(0)  # steps it takes for x to get to 1
    loses = int(1)  # game over tracker to tease the player with # of losses lol
    delay = float(1)  # delay is reduced each game until cache_max is fulfilled
    new_color = '\033[0;30;43m'
    color_reset = '\033[0;37;40m'
    box_color = '\033[0;30;47m'
    green_box = '\033[0;37;42m'
    red_box = '\033[0;37;41m'
    green_text = '\033[1;32;40m'
    red_text = '\033[1;31;40m'
    box = ' ' * 11  # game over box borders (top and bottom)
    x = int(x)  # convert input x to int

    while True:  # game loop continues forever because this game cannot be won
        new_value = x

        # print new value at start of new game
        print(f'\n{new_color}New Value: {color_reset}\n{x}\n')

        # calculation loop
        while x != 1:  # equation loop until x reaches 1 (which causes an infinite loop 4->2->1 thus game over)
            steps += 1
            if x % 2 == 0:  # if x is even divide by 2
                x = x // 2
                print(f'{red_box}  {color_reset} {steps}\t\b{red_text}{x}{color_reset}')
            else:  # if x is odd, multiply by 3 and add 1
                x = 3 * x + 1
                print(f'{green_box}  {color_reset} {steps}\t\b{green_text}{x}{color_reset}')
            time.sleep(delay * .05)  # delay between each run of the equation 

        # if current score is higher than recorded score, update recorded to current
        if steps > current_score:
            current_score = steps

        # if highscore in log file is higher than current score, update current
        if highscore > current_score:
            current_score = highscore

        # else set current score as new highscore in log file
        elif highscore < current_score:
            highscore = current_score  # this line is needed to prevent log file from giving incorrect seed #
            record.close()  # close log file (in read mode)
            record = open(log, 'w')  # open log file (in write mode)
            record.writelines([f'Best Seed: {new_value}\nHighscore: {current_score}'])  # write new seed & score
        record.close()  # close log file (in write mode), reopens at beginning of new game

        # game over screen
        print(f'''
{box_color}{box}{color_reset}
{box_color} GAME OVER {color_reset}
{box_color}{box}{color_reset}

{box_color}Wins:      {color_reset}
0
{box_color}Loses:     {color_reset}
{loses}
{box_color}High Score:{color_reset}
{current_score}\n''')

        x = new_value + 1  # add 1 to previous input/new value to progress the game to next number
        loses += 1  # records losses in the session, displays them in the game over screen
        steps = int(0)  # reset current score for new game
        time.sleep(delay * .75)
        clear()


start()
clear()
game(input('Please enter your desired seed(number):\n\n'))
