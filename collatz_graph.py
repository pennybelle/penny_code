import matplotlib.pyplot as plt
from sys import setrecursionlimit
setrecursionlimit(10_000)

def collatz(x, step=0):
    if step > 9993: # prevents error when stack is abt to overflow
        print(f'{x} exceeded recursion depth of 10000')
        exit()
    elif x == 1: # ends the recursion, returns the score (how many steps)
        return step
    elif x % 2 == 0: # if even, divide by 2
        return collatz(x // 2, step + 1)
    else: # if odd, multiply by 3 and add 1
        return collatz(3 * x + 1, step + 1)

def run_collatz(x, rng, y_points=[]): # run the conjecture in a loop
    for i in range(x, rng): # test loop
        step = collatz(x) # runs the conjecture recursion function 
        y_points.append(step)
        # print(f'{x:,}') # debug
        x += 1 # move to next integer to test 
    # if x > rng:
    #     y_points.append(collatz(x))
    #     return run_collatz(x+1, rng, y_points)
    return y_points
        

def plot_points(start_val, stop_val):
    x_points = [x for x in range(start_val, stop_val)]
    y_points = run_collatz(start_val, stop_val)
    print('Coordinates calculated, plotting...')

    plt.plot(x_points, y_points, linewidth=1)
    plt.title(f'Collatz Conjecture | Testing {start_val:,} to {stop_val:,}')
    plt.xlabel("Loop Start Value")
    plt.ylabel("Loop Range")
    plt.show()

plot_points(1, 1_000)
