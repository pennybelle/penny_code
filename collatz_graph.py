import csv
from sys import argv
import matplotlib.pyplot as plt
from sys import setrecursionlimit
setrecursionlimit(10_000)

global_cache = {}

def collatz(x, step=0):
    # print(x, step) # debug
    if step > 9993: exit() # prevents stack overflow
    elif x in global_cache.keys(): 
        # print('known path', x, cache[x])
        return step + global_cache[x]
    elif x == 1: # ends the recursion, returns the score (how many steps)
        # print('new path', cache['paths'])
        return step
    elif x % 2 == 0: # if even, divide by 2
        return collatz(x // 2, step + 1)
    else: # if odd, multiply by 3 and add 1
        return collatz(3 * x + 1, step + 1)

def run_collatz(x, rng, cache): # run the conjecture in a loop
    paths = 0 # TODO: unique pathfinder
    y_points = []
    for x in range(x, rng):
        if str(x) in cache.keys(): # if x already cached, import data
            print('Importing data...')
            y_points.append(cache[str(x)])
            print(f'Data imported...{x}')
            continue
        step = collatz(x)
        y_points.append(step) # conjecture recursion function
        cache[x] = step # new cache entry
    # if x > rng: # tail recursion test
    #     y_points.append(collatz(x))
    #     return run_collatz(x+1, rng, y_points)
    return y_points

def plot_points(start_val, stop_val):
    with open('cache.csv') as file:
        data = csv.reader(file)
        cache = dict(data)
        print('Cache imported, running calculations...')
    y_points = run_collatz(start_val, stop_val, cache)
    x_points = [x for x in range(start_val, stop_val)]
    print('Calculations complete...')
    print('Merging caches...')
    global_cache.update(cache)
    print('Plotting coordinates...')
    plt.plot(x_points, y_points, linewidth=1)
    plt.title(f'Collatz Conjecture | Testing {start_val:,} to {stop_val:,}')
    plt.xlabel("Loop Start Value")
    plt.ylabel("Loop Range")
    cache_data()
    plt.show()

def cache_data():
    with open('cache.csv') as file:
        data = csv.reader(file)
        old_cache = dict(data)
    with open('cache.csv', 'w') as file:
        write_data = csv.writer(file)
        for key, value in global_cache.items():
            if not key in old_cache.keys(): write_data.writerow([key, value])
        print('Cache saved...')


plot_points(1, 1_000_000)
# print(cache) # debug

