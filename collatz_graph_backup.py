# import csv
# from sys import argv
# import matplotlib.pyplot as plt
# from sys import setrecursionlimit
# setrecursionlimit(10_000)

# global_cache = {}

# def collatz(x, step=0, new_path=False):
#     # print(x, step) # debug
#     if step > 9993: exit() # prevents stack overflow
#     elif not x in (4, 2, 1) and x in global_cache.keys(): 
#         # print('known path', x, cache[x])
#         return step + global_cache[x], new_path
#     elif x == 1: # ends the recursion, returns the score (how many steps)
#         # print('new path', cache['paths'])
#         new_path = True
#         return step, new_path
#     elif x % 2 == 0: # if even, divide by 2
#         return collatz(x // 2, step + 1)
#     else: # if odd, multiply by 3 and add 1
#         return collatz(3 * x + 1, step + 1)

# def run_collatz(x, rng, cache): # run the conjecture in a loop
#     paths = 0
#     y_points = []
#     for x in range(x, rng): # test loop
#         step, new_path = collatz(x)
#         y_points.append(step) # conjecture recursion function
#         if new_path: paths += 1
#         if not x in cache.keys(): cache[x] = step # new cache entry
#     # if x > rng: # tail recursion test
#     #     y_points.append(collatz(x))
#     #     return run_collatz(x+1, rng, y_points)
#     return y_points, paths

# def plot_points(start_val, stop_val):
#     with open('cache.csv') as file:
#         data = csv.reader(file)
#         cache = dict(data)
#     y_points, paths = run_collatz(start_val, stop_val, cache)
#     x_points = [x for x in range(start_val, stop_val)]
#     global_cache['paths'] = paths
#     global_cache.update(cache)
#     print('Coordinates calculated, plotting...')
#     plt.plot(x_points, y_points, linewidth=1)
#     plt.title(f'Collatz Conjecture | Testing {start_val:,} to {stop_val:,} | Total Unique Paths: {paths}')
#     plt.xlabel("Loop Start Value")
#     plt.ylabel("Loop Range")
#     cache_data()
#     plt.show()

# def cache_data():
#     with open('cache.csv') as file:
#         data = csv.reader(file)
#         old_cache = dict(data)
#     with open('cache.csv', 'w') as file:
#         write_data = csv.writer(file)
#         for key, value in global_cache.items():
#             if not key in old_cache.keys(): write_data.writerow([key, value])
#         print('Cache saved...')


# plot_points(25, 100)
# # print(cache) # debug

import matplotlib.pyplot as plt
from time import time
from sys import setrecursionlimit
setrecursionlimit(10_000)

class collatz(dict):

    def __getitem__(self, x):
        val = self.get(x, None)
        if val is None:
            seq_len = self.calc_seq_len(x)
            self[x] = seq_len
            return seq_len
        return val
    
    def calc_seq_len(self, x):
        if x in self:
            self[x] = self[x] + 1
            return self[x]
        if x ==1:
            self[x] = 0
            return 0
        
        seq_freq = self.calc_seq_len(x*3+1 if x%2 else x//2) + 1
        self[x] = seq_freq

        return seq_freq

    # def __init__(self):
    #     self.cache = {}

    # def cullCache(self):
    #     temp = {}
    #     for pair in self.cache.items():
    #         if pair[1][1] != 1:
    #             #del self.cache[pair[0]]
    #             temp[pair[0]] = [pair[1][0], pair[1][1]]
    #     self.cache = temp


# # TODO: add a hit counter and cull entries with 1 hit every 50,000,000 steps
    # def collatz(self, x):
    #     if x % 10_000_000 == 0: 
    #         print('Culling cache...')
    #         self.cullCache()
    #     if x in self.cache:
    #         self.cache[x][1] = self.cache[x][1]+1
    #         return self.cache[x][0]
    #     elif x == 1:
    #         self.cache[x] = [0, 1]
    #         return 0
        
    #     seq_freq = self.collatz(x*3+1 if x%2 else x//2) + 1
    #     self.cache[x] = [seq_freq, 1]

    #     return seq_freq


    # def plot_collatz(self, i, j, display=True, save=False):
    #     print(f'Running calculations for {i:,} through {j:,}...')
    #     timer_start = time() # timer
    #     y_points = [self.collatz(i) for i in range(i, j)] # list of sequence lengths in order of x ascending
    #     timer_stop = time() - timer_start
    #     x_points = [x for x in range(i, j)] # set x points using a ranged list comprehension of x thru rng
    #     print(f'Took {timer_stop:.2f} seconds...')

    #     print('Dumping cache...')
    #     self.cache.clear() # sweet relief

    #     print('Plotting coordinates...')
    #     plt.plot(x_points, y_points, marker=',', linestyle='')
    #     plt.xlabel('Loop Start Value') # set X axis label on graph
    #     plt.ylabel('Loop Range') # set Y axis label on graph
    #     plt.title(f'Collatz Conjecture [{i:,}, {j:,}] | Calculations took {timer_stop:.1f} secs')

    #     if save:
    #         print('Saving plot to image...')
    #         plt.savefig(f'Collatz_Array_{i}_{j}_{timer_stop:.0f}secs.png') # save graph to png

    #     if display:
    #         print('Displaying plot...')
    #         plt.show() # show graph in gui


    # def plot_seq_len(self, i, j, display=True, save=False):
    #     print(f'Running Calculations for {i:,} through {j:,}...')
    #     timer_start = time() # timer
    #     seq_list = [self.collatz(i) for i in range(i, j)] # list of sequence lengths in order of x ascending
    #     timer_stop = time() - timer_start
    #     print(f'Took {timer_stop:.2f} seconds...')

    #     print('Dumping cache...')
    #     self.cache.clear() # sweet relief

    #     print('Analyzing Frequency of Sequence Lengths...')
    #     data = {} # make dict that tracks instances of seq in seq_list
    #     for seq in seq_list:
    #         if seq in data: data[seq] += 1
    #         else: data[seq] = 1

    #     print('Sorting and dumping local data...')
    #     data = sorted(list(data.items())) # convert dict(data) to sorted list of dict(data) contents
    #     x_points, y_points = [float(t[0]) for t in data], [float(t[1]) for t in data] # parse data from nested tuples to 2 lists
    #     data = [] # dump old data for memory optimization

    #     print('Plotting coordinates...')
    #     plt.plot(x_points, y_points, marker='.', markersize=1, linestyle='')
    #     plt.xlabel('Sequence Length') # set X axis label on graph
    #     plt.ylabel('Frequency') # set Y axis label on graph
    #     plt.title(f'Sequence Length Analysis [{i:,}, {j:,}] | Calculations took {timer_stop:.1f} secs')

    #     if save:
    #         print('Saving plot to image...')
    #         plt.savefig(f'Collatz_Array_SFA_{i}_{j}_{timer_stop:.0f}secs.png') # save graph to png

    #     if display:
    #         print('Displaying plot...')
    #         plt.show() # show graph in gui


def plotter(title, x, y, xlab, ylab, marker=',', markersize=2, linestyle=''):
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.plot(x, y, marker, markersize, linestyle)
    plt.show()


def plot_seq_len(i, j):
    start = time()
    c = collatz()
    for x in range(i, j+1):
        s = c[x]
    print(f'Duration of calculation: {time() - start} sec')

    title = f'Collatz Stopping Time Analysis (max={x:,})'
    xlab = 'Stopping Time'
    ylab = 'Frequency'
    points = {}
    for v in c.values():
        points[v] = points[v] + 1
    plotter(title, points.keys(), points.values(), xlab, ylab)


# cg().plot_collatz(1, 10_000_000, display=True, save=False)
plot_seq_len(1, 10_000_000)
