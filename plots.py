import math

import matplotlib.pyplot as plt
import numpy as np


# Calc value of a linear function
def calc_func_val(tan, dist_x, dist_y, val):
    return (tan * (val - dist_x)) + dist_y


# Draw approximated points with
def draw_points(x_arr, y_arr, dist_x, dist_y):
    ax = plt.subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                     box.width, box.height * 0.9])

    # Draw approximated points from each angle pair
    plt.scatter(x=x_arr, y=y_arr, facecolors='none', edgecolors='r', label='Approximated position of transmitter',
                    zorder=10)
    plt.scatter(x='0', y='0', color='g', marker='o', label="Receiver position", zorder=10)
    plt.scatter(x=dist_x, y=dist_y, color='g', marker='o', zorder=10)

    plt.xlabel('x')
    plt.xlabel('y')
    plt.title('Approximated positions of transmitter: ')

    plt.xlim(-2, 3)
    plt.ylim(-2, 2)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
               fancybox=True, ncol=2)
    plt.show()


def draw_linear_functions(tan1, tan2, dist_x, dist_y, x, y):
    ax = plt.subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                     box.width, box.height * 0.9])

    # Prepare linear functions
    x_values = np.linspace(-15, 15, 10000)
    y_values_1 = []
    y_values_2 = []

    for val in x_values:
        y_values_1.append(calc_func_val(tan1, 0, 0, val))
        y_values_2.append(calc_func_val(tan2, dist_x, dist_y, val))

    plt.scatter(x='0', y='0', color='g', marker='o', label="Receiver position", zorder=10)
    plt.scatter(x=dist_x, y=dist_y, color='g', marker='o', zorder=10)
    plt.scatter(x=x, y=y, color='black', marker='x', label="Approximated transmitter position", zorder=10)

    plt.plot(x_values, y_values_1, 'r', label='R1', zorder=0)
    plt.plot(x_values, y_values_2, 'b', label='R2', zorder=0)

    plt.xlabel('x')
    plt.xlabel('y')
    plt.title('Linear Functions for filtered avg angles: ')

    plt.xlim(-2, 3)
    plt.ylim(-2, 2)

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
               fancybox=True, ncol=2)
    plt.show()


def draw_linear(x_arr, y_arr, dist_x, dist_y):
    ax = plt.subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                     box.width, box.height * 0.9])

    plt.scatter(x='0', y='0', color='g', marker='o', label="Receiver position", zorder=10)
    plt.scatter(x=dist_x, y=dist_y, color='g', marker='o', zorder=10)

    plt.plot(x_arr, y_arr, 'r', label='R1', zorder=0)
    plt.xlabel('x')
    plt.xlabel('y')
    plt.title('Approximated positions of transmitter: ')

    plt.xlim(-2, 3)
    plt.ylim(-2, 2)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
               fancybox=True, ncol=2)
    plt.show()
