import matplotlib.pyplot as plt
from time import time
from sys import setrecursionlimit
setrecursionlimit(10_000)

class cg():
    def __init__(self):
        self.cache = {}


    def collatz(self, x): # TODO: recursively build cache up backwards
        if x in self.cache:  
            return self.cache[x]
        elif x == 1: # ends the recursion, returns the sequence length
            self.cache[x] = 0
            return 0
        seq_freq = self.collatz(x//2 if x%2 == 0 else x*3+1) + 1
        self.cache[x] = seq_freq
        return seq_freq


    def collatz_range(self, x, rng): # run the conjecture in a loop
        seq_len_list = []
        # paths = 0 # TODO: unique pathfinder

        # if x > 1:
        #     for i in range(1, x):
        #         self.collatz(i)

        for x in range(x, rng):
            seq_len = self.collatz(x) # conjecture recursion function
            seq_len_list.append(seq_len)
            # print(self.cache)
            # self.cache[x] = seq_len

        return seq_len_list


    def plot_collatz(self, start, stop, display=True, save=False):
        print(f'Running calculations for {start:,} through {stop:,}...')
        start_time = time()
        y_points = self.collatz_range(start, stop)
        secs = time() - start_time # keep track of calculation time
        x_points = [x for x in range(start, stop)]
        print(f'Took {secs:.2f} seconds...')

        print('Dumping cache...')
        self.cache.clear() # sweet relief

        print('Plotting coordinates...')
        plt.plot(x_points, y_points, marker=',', linestyle='')
        plt.xlabel('Loop Start Value') # set X axis label on graph
        plt.ylabel('Loop Range') # set Y axis label on graph
        plt.title(f'Collatz Conjecture [{start:,}, {stop:,}] | Calculations took {secs:.1f} secs')

        if save:
            print('Saving plot to image...')
            plt.savefig(f'Collatz_Array_{start}_{stop}_{secs:.0f}secs.png') # save graph to png

        if display:
            print('Displaying plot...')
            plt.show() # show graph in gui


    def plot_seq_len(self, start, stop, display=True, save=False):
        print(f'Running Calculations for {start:,} through {stop:,}...')
        start_time = time()
        seq_len_list = self.collatz_range(start, stop)
        secs = time() - start_time # keep track of calculation time
        print(f'Took {secs:.2f} seconds...')

        print('Dumping cache...')
        self.cache.clear() # sweet relief

        print('Parsing data...')
        data = {}
        for seq_len in seq_len_list:
            if seq_len in data: data[seq_len] += 1
            else: data[seq_len] = 1

        print('Sorting data and dumping local data...')
        data = sorted(list(data.items())) # convert dict(data) to sorted list of dict(data) contents
        x_points = [float(t[0]) for t in data] # parse nested tuples for value in index 0
        y_points = [float(t[1]) for t in data] # parse nested tuples for value in index 1
        data = [] # dump old data for memory optimization

        print('Plotting coordinates...')
        plt.plot(x_points, y_points, marker='.', markersize=1, linestyle='')
        plt.xlabel('Sequence Length') # set X axis label on graph
        plt.ylabel('Frequency') # set Y axis label on graph
        plt.title(f'Sequence Length Analysis [{start:,}, {stop:,}] | Calculations took {secs:.1f} secs')

        if save:
            print('Saving plot to image...')
            plt.savefig(f'Collatz_Array_SFA_{start}_{stop}_{secs:.0f}secs.png') # save graph to png

        if display:
            print('Displaying plot...')
            plt.show() # show graph in gui


# cg().plot_collatz(1, 10_000_000, display=True, save=False)
cg().plot_seq_len(1, 100_000_000, display=True, save=True)

# while True:
#     start = int(input('Start Value: ').replace(',', ''))
#     stop = int(input('Stop Value: ').replace(',', ''))
#     choice = input('Choose Plot Type:\n\t'
#                    '[c] Original Collatz Conjecture\n\t'
#                    '[s] Sequence Frequency Analysis\n').lower()
    
#     # wider gap between values leads to larger memory usage
#     if choice == 'c': cg().plot_collatz(start, stop, display=True, save=False)

#     elif choice == 's': cg().plot_seq_freq(start, stop, display=True, save=False)

#     elif choice in ('e', 'exit', 'quit'): break
#     else: print('Invalid entry...')
