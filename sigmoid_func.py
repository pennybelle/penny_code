import matplotlib.pyplot as plt 
import numpy as np
from scipy.interpolate import make_interp_spline

e = 2.718282

def sig(t):
    return 1/(1+(e**-t))

def plot_points(s, t):
    x_list = [x for x in range(s, t)]
    y_list = []
    for i in range(s, t):
        y_list.append(sig(i))

    x_array, y_array = np.array(x_list), np.array(y_list)
    spline = make_interp_spline(x_array, y_array)
    x = np.linspace(x_array.min(), x_array.max(), 500)
    y = spline(x)


    plt.plot(x, y)
    plt.title('Sigma Function')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

plot_points(-10, 10)