from functools import cache
import matplotlib.pyplot as plt
from sys import setrecursionlimit
setrecursionlimit(10_000)

@cache
def collatz(x, step=0):
    if x == 1: # ends the recursion, returns the score (how many steps)
        return step
    elif x % 2 == 0: # if even, divide by 2
        x //= 2
    else: # if odd, multiply by 3 and add 1
        x = x * 3 + 1
    step += 1
    return collatz(x, step)

def run_collatz(x, rng): # run the conjecture in a loop
    # paths = 0 # TODO: unique pathfinder
    y_points = []
    for x in range(x, rng):
        step = collatz(x)
        y_points.append(step) # conjecture recursion function
    return y_points

def plot_points(start_val, stop_val):
    print(f'Running calculations for {start_val:,} through {stop_val:,}...')
    y_points = run_collatz(start_val, stop_val)
    x_points = [x for x in range(start_val, stop_val)]
    print('Plotting coordinates...')
    plt.plot(x_points, y_points, marker=',', linestyle='')
    plt.title(f'Collatz Conjecture | Testing {start_val:,} to {stop_val:,}')
    plt.xlabel("Loop Start Value")
    plt.ylabel("Loop Range")
    print('Saving plot...')
    plt.savefig(f'Collatz_Array_{start_val}_{stop_val}.png') # save graph to png
    # plt.show() # show graph in gui

def plot_step_freq(start_val, stop_val):
    print(f'Running calculations for {start_val:,} through {stop_val:,}...')
    x_points = run_collatz(start_val, stop_val)
    y_points = [y for y in range(start_val, stop_val)]
    print('Plotting coordinates...')
    plt.plot(x_points, y_points, marker=',', linestyle='')
    plt.title(f'Collatz Conjecture Step Frequency | Plotting {start_val:,} to {stop_val:,}')
    plt.xlabel(f"X")
    plt.ylabel("Number of steps for X to reach 1")
    print('Saving plot...')
    plt.savefig(f'Collatz__Step_Freq_Array_{start_val}_{stop_val}.png') # save graph to png

plot_step_freq(1, 1_000_000) 
# plot_points(1, 1_000_000) # for stable execution do not exceed a 1,000,000 unit gap

def multi_plot(multiplier, start_val, stop_val):
    addition = stop_val
    for x in range(multiplier):
        plot_points(start_val, stop_val)
        start_val = stop_val + 1
        stop_val += addition

multi_plot(10, 1, 1_000_000)
