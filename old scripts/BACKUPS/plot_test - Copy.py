
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
style.use('ggplot')
plt.ylabel('y')
plt.xlabel('x')
y = int(2)
plt.plot(y)
while True:
    x = int(y + 1)
    plt.plot(x)
    print("NEW VALUE - " + str(int(x)))
    while x != 1:
        if int(x % 2) == 0:
            x /= int(2)
            print("DOWN - " + str(int(x)))
            plt.plot(x)
            continue
        elif int(x % 2) != 0:
            x = int(3 * x + 1)
            print("UP - " + str(int(x)))
            plt.plot(x)
            continue
    while x == 1:
        print("-----------\nGAME OVER\n-----------")
        break
    y += int(1)
    plt.plot(y)
    continue

def animate