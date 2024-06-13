
import os
def clear(): os.system('cls')

y = [1]

while True:
    print(y)
    y.insert(0, y[0] + 1)
    del y[1]
    clear()
    continue
