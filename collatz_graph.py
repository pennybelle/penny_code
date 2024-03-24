import matplotlib.pyplot as plt
from time import time
from sys import setrecursionlimit
setrecursionlimit(10_000)

class cg():
    def __init__(self):
        self.global_cache = {}

    def collatz(self, x, step=0):
        if x in self.global_cache.keys():  
            return step + self.global_cache[x]
        elif x == 1: # ends the recursion, returns the score (how many steps)
            return step
        elif x % 2 == 0: # if even, divide by 2
            x //= 2
        else: # if odd, multiply by 3 and add 1
            x = x * 3 + 1
        step += 1

        return self.collatz(x, step)

    def run_collatz(self, x, rng, cache): # run the conjecture in a loop
        y_points = []
        # paths = 0 # TODO: unique pathfinder

        for x in range(x, rng):
            step = self.collatz(x)
            y_points.append(step) # conjecture recursion function
            if not x in cache.keys(): self.global_cache[x] = step

        return y_points

    def plot_collatz(self, start, end, display=True, save=False):
        print(f'Running calculations for {start:,} through {end:,}...')
        start_time = time()
        y_points = self.run_collatz(start, end, self.global_cache)
        secs = time() - start_time # keep track of calculation time
        x_points = [x for x in range(start, end)]
        print(f'Took {secs:.2f} seconds...')

        print('Dumping cache...')
        self.global_cache.clear() # sweet relief

        print('Plotting coordinates...')
        plt.plot(x_points, y_points, marker=',', linestyle='')
        plt.xlabel('Loop Start Value') # set X axis label on graph
        plt.ylabel('Loop Range') # set Y axis label on graph
        plt.title(f'Collatz Conjecture | Plotting {start:,} to {end:,} | Calculations took {secs:.1f} secs')

        if save:
            print('Saving plot to image...')
            plt.savefig(f'Collatz_Array_{start}_{end}_{secs:.0f}secs.png') # save graph to png

        if display:
            print('Displaying plot...')
            plt.show() # show graph in gui

    def plot_step_freq(self, start, end, display=True, save=False):
        print(f'Running Calculations for {start:,} through {end:,}...')
        start_time = time()
        steps = self.run_collatz(start, end, self.global_cache)
        secs = time() - start_time # keep track of calculation time
        print(f'Took {secs:.2f} seconds...')

        print('Dumping cache...')
        self.global_cache.clear() # sweet relief

        print('Parsing data...')
        data = {}
        for step in steps:
            if step in data:
                data[step] += 1
            else:
                data[step] = 1

        print('Sorting data and dumping local cache...')
        data = sorted(list(data.items())) # convert dict(data) to sorted list of dict(data) contents
        x_points = [float(t[0]) for t in data] # parse nested tuples for value in index 0
        y_points = [float(t[1]) for t in data] # parse nested tuples for value in index 1
        data = [] # dump old data for memory optimization

        print('Plotting coordinates...')
        plt.plot(x_points, y_points, marker='.', markersize=1, linestyle='')
        plt.xlabel('Sequence Length') # set X axis label on graph
        plt.ylabel('Frequency') # set Y axis label on graph
        plt.title(f'Collatz Conjecture | Sequence Length Analysis [{start}, {end}] | Calculations took {secs:.1f} secs')

        if save:
            print('Saving plot to image...')
            plt.savefig(f'Collatz_Array_SFA_{start}_{end}_{secs:.0f}secs.png') # save graph to png

        if display:
            print('Displaying plot...')
            plt.show() # show graph in gui

cg().plot_step_freq(1, 10_000_000, display=True, save=False)
# cg().plot_collatz(1, 1_000_000, display=True, save=True) # for stable execution do not exceed a 1,000,000 unit gap
