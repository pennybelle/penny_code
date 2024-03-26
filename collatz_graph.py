import matplotlib.pyplot as plt
from time import time

class collatz(dict): # subclass dict is used as cache

    def __getitem__(self, x):
        v = self.get(x, None) # value (v) is cache dict[x] if not None else dict[x] = None
        if not v is None: return v # if x is in cache return value at key x
        v = self.calc_seq(x) # else set value using conjecture function
        self[x] = v # then fill cache dict[x] with value (v)
        return v # return value of cache dict[x]

    def calc_seq(self, x, steps=0):
        if x == 1: return steps # guard clause
        x = x//2 if x%2 == 0 else x*3+1 # conjecture function
        steps += 1 # sequence length tracker
        v = self.get(x, None) # v is class dict[x] if not None else dict[x] = None
        if v is None: return self.calc_seq(x, steps) # if x not in cache, recurse  
        return steps + v # else return tracker + cached seq length for v


def plotter(title, x, y, xlab, ylab, marker='.', markersize=1, linestyle=''):
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.plot(x, y, marker, markersize, linestyle)
    plt.savefig(title+'.png')
    plt.show()

def run_val(i, j): # run conjecture in range of i & j
    start = time() # timer
    c = collatz() # set class dict to var for reference
    for x in range(i, j+1): c[x] # fill cache.dict[i through j+1]
    t = time() - start # timer results
    print(f'Calculation duration: {t:.2f} sec')
    return c, t # return cache,dict for reference as well as timer results

def plot_seq_len(i, j):
    c, t = run_val(i, j) # referencing collatz dict to var & fills cache
    title = f'Collatz Sequence Length Analysis [{i:,}, {j:,}] {t:.0f}secs'
    xlab = 'Sequence Length'
    ylab = 'Frequency'
    points = {} # local cache for frequency analysis of sequence lengths in cache.dict.values
    for v in c.values(): points[v] = points.setdefault(v, 0) + 1 # seq freq analysis algo
    c.clear() # dump cache
    plotter(title, points.keys(), points.values(), xlab, ylab) # plot results on graph

plot_seq_len(1, 1_000_000)
