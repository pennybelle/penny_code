import sys
sys.setrecursionlimit(2000)
# import curses
# from curses import wrapper
# stdstr = curses.initscr()
# curses.noecho()
# curses.cbreak()
# stdstr.keypad(True)

def collatz(x=300339047, step=0): # x default is highest seed b4 stack overflow
    if step > 993: # prevents error when stack is abt to overflow
        print(f'{x} exceeded recursion depth of 1000')
        exit()
    elif x == 1: # ends the recursion, returns the score (how many steps)
        return step
    elif x % 2 == 0: # if even, divide by 2
        return collatz(x // 2, step + 1)
    else: # if odd, multiply by 3 and add 1
        return collatz(3 * x + 1, step + 1)

def run_collatz(x): # run the conjecture in a loop
    most_steps = 0 # keeps score of most steps taken to get from x to 1
    best_seed = 0
    while True: # infinite loop to continuously test
        steps = collatz(x) # runs the conjecture recursion function
        if steps > most_steps: # sets new score if higher than previous
            most_steps = steps
            best_seed = x
        print(f'{x}: {steps}\tsteps   |   most steps taken = {most_steps}  |  best seed = {best_seed}')
        x += 1 # move to next integer to test
    
run_collatz(1) # run the infinite test loop
# x: steps