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
    
    print(collatz(121))

    def run_collatz(self, x, rng, cache): # run the conjecture in a loop
        y_points = []
        # paths = 0 # TODO: unique pathfinder

        for x in range(x, rng):
            step = self.collatz(x)
            y_points.append(step) # conjecture recursion function
            if not x in cache.keys(): self.global_cache[x] = step

        return y_points

    def plot_points(self, start_val, stop_val, display=True, save=False):
        print(f'Running calculations for {start_val:,} through {stop_val:,}...')
        start_time = time()
        y_points = self.run_collatz(start_val, stop_val, self.global_cache)
        time_taken = time() - start_time
        x_points = [x for x in range(start_val, stop_val)]
        print(f'Took {time_taken:.2f} seconds...')

        print('Dumping cache...')
        self.global_cache.clear()

        print('Plotting coordinates...')
        plt.plot(x_points, y_points, marker=',', linestyle='')
        plt.xlabel('Loop Start Value') # set X axis label on graph
        plt.ylabel('Loop Range') # set Y axis label on graph
        plt.title(f'Collatz Conjecture | Plotting {start_val:,} to {stop_val:,} | Calculations took {time_taken:.1f} secs')

        if save:
            print('Saving plot to image...')
            plt.savefig(f'Collatz_Array_{start_val}_{stop_val}_{time_taken:.0f}secs.png') # save graph to png

        if display:
            print('Displaying plot...')
            plt.show() # show graph in gui

    def step_freq(self, start_val, stop_val):
        print(f'Running Calculations for {start_val:,} through {stop_val:,}...')
        steps = self.run_collatz(start_val, stop_val, self.global_cache)
        data = {}

        for step in steps:
            if step in data:
                data[step] += 1
            else:
                data[step] = 1

        return data

    def plot_step_freq(self, start_val, stop_val, display=True, save=False):
        print(f'Running Calculations for {start_val:,} through {stop_val:,}...')
        start_time = time()
        steps = self.run_collatz(start_val, stop_val, self.global_cache)
        time_taken = time() - start_time
        print(f'Took {time_taken:.2f} seconds...')

        print('Parsing data...')
        data = {}
        for step in steps:
            if step in data:
                data[step] += 1
            else:
                data[step] = 1

        print('Dumping cache and sorting data...')
        data = sorted(list(data.items()))
        x_points = [float(t[0]) for t in data]
        y_points = [float(t[1]) for t in data]

        # print(x_points)
        # print(y_points)

        print('Plotting coordinates...')
        plt.plot(x_points, y_points, marker=',', linestyle='')
        plt.xlabel('Loop Length') # set X axis label on graph
        plt.ylabel('Frequency') # set Y axis label on graph
        plt.title(f'Collatz Conjecture | Iteration Frequency Analysis | Calculations took {time_taken:.1f} secs')

        if save:
            print('Saving plot to image...')
            plt.savefig(f'Collatz_Array_IFA_{start_val}_{stop_val}_{time_taken:.0f}secs.png') # save graph to png

        if display:
            print('Displaying plot...')
            plt.show() # show graph in gui

cg().plot_step_freq(1, 10_000_000, display=True, save=False)
# cg().plot_points(1, 1_000_000, display=True, save=True) # for stable execution do not exceed a 1,000,000 unit gap
