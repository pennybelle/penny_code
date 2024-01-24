from math import log

n = 2
s = .75

d = log(n) / log(s)


print(d)

def fractal(n, s):
    return log(n) / log(s)

for n in range(1, 25):
    print(fractal(n, s))