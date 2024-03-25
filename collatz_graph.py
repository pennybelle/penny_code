import matplotlib.pyplot as plt
from time import time

class collatz(dict):

    def __getitem__(self, x):
        v = self.get(x, None)
        if v is None:
            v = self.calc_seq(x)
            self[x] = v
        return v

    def calc_seq(self, x, steps=0):
        if x == 1:
            return steps
        x = x//2 if x%2 == 0 else x*3+1 # collatz function
        steps += 1
        
        v = self.get(x, None)
        if v is None:
            return self.calc_seq(x, steps)    
        return steps + v


def plotter(title, x, y, xlab, ylab, 
            marker='.', markersize=1, linestyle='', 
            display=True, save=True):
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.plot(x, y, marker, markersize, linestyle)
    if save: plt.savefig(title+'.png')
    if display: plt.show()

def run_val(i, j): # run conjecture in loop of i & j
    start = time()
    c = collatz() # set class dict to var for reference
    for x in range(i, j+1):
        c[x] # reference dict[x] to init conjecture algo
    t = time() - start
    print(f'Calculation duration: {t:.2f} sec')
    return c, t # return class dict for reference

def plot_seq_len(i, j):
    c, t = run_val(i, j) # referencing collatz dict to var & fills cache
    title = f'Collatz Sequence Length Analysis [{i:,}, {j:,}] {t:.0f}secs'
    xlab = 'Sequence Length'
    ylab = 'Frequency'
    points = {}
    for v in c.values():
        points[v] = points.setdefault(v, 0) + 1 # seq freq analysis
    c.clear() # dump cache
    plotter(title, points.keys(), points.values(), xlab, ylab)


plot_seq_len(1, 200_000_000)
