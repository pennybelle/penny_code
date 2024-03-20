import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt 

def base_e(n):
    return (1+(1/n))**n

def plot_base_e(transform=1, rng=11):
    x_list = []
    y_list = []

    for n in range(1, rng):
        x_list.append(n)
        y_list.append(base_e(n*transform))

    print(y_list[-1])

    x_array = np.array(x_list)
    y_array = np.array(y_list)
    spline = make_interp_spline(x_array, y_array)
    x = np.linspace(x_array.min(), x_array.max(), 500)
    y = spline(x)

    plt.plot(x, y)
    plt.xscale('log')
    plt.xticks('log')
    plt.title("Euler's Constant | e = (1+(1/n))^n | The Logarithmic Curve Of e")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

plot_base_e(transform=0.001, rng=10000)