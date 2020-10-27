#! env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys, heapq, bisect, math, itertools, string, queue, datetime, unittest
import numpy as np
import matplotlib.pyplot as plt
import pprint


# ctci.7_6
# Given a two-dimensional graph with points on it, find a line which passes the most number of points.
# Date: 2020/10/25
# Author: koucs

def find_best_line(points: np.array) -> (float, float, bool):
    best_line = None
    line_count = {}
    for i in range(len(points[0])):
        for j in range(i + 1, len(points[0])):
            line = Line(points[0][i], points[1][i], points[0][j], points[1][j])
            if line not in line_count.keys():
                line_count[line] = 0
            line_count[line] += 1
            if best_line is None or line_count[line] > line_count[best_line]:
                print(points[0][i], points[1][i], points[0][j], points[1][j])
                best_line = line
    pprint.pprint(line_count)
    pprint.pprint(best_line)
    return best_line.sl, best_line.yi, best_line.is_inf_sl


def is_equal(a, b):
    return abs(a - b) < sys.float_info.epsilon


class Line():
    is_inf_sl = False  # infinite slope
    sl = 0.0  # slope
    yi = 0.0  # y_intercept

    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        if abs(x1 - x2) < sys.float_info.epsilon:
            self.is_inf_sl = True
            self.yi = x1
        else:
            self.sl = (y1 - y2) / (x1 - x2)
            self.yi = y1 - self.sl * x1

    def __eq__(self, other):
        if is_equal(self.sl, other.sl) and is_equal(self.yi, other.yi) and self.is_inf_sl == other.is_inf_sl:
            return True
        return False

    def __hash__(self):
        # Bit OR
        # 1000かけている理由は、少数の
        return int(self.sl * 1000) | int(self.yi * 1000)


if __name__ == '__main__':

    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.grid()
    ax.set_xlim([0, 50])
    ax.set_ylim([0, 50])
    ax.set_xlabel("x", fontsize=14)
    ax.set_ylabel("y", fontsize=14)

    N = 10
    x = np.random.randint(low=0, high=50, size=N)
    y = np.random.randint(low=0, high=50, size=N)
    points = np.array([x, y])
    print(points)
    ax.scatter(x, y)
    for i in range(N):
        ax.text(x[i], y[i], '({x}, {y})'.format(x=x[i], y=y[i]), fontsize=7)

    slope, y_intercept, infinite_slope = find_best_line(points)
    if not infinite_slope:
        x = np.linspace(0, 100)
        ax.plot(x, slope * x + y_intercept, '-g')  # solid green
        ax.text(0, y_intercept, 'y = {a}x + {b}'.format(a=slope, b=y_intercept), fontsize=7)
    else:
        ax.axvline(x=y_intercept)  # solid green
        ax.text(0, y_intercept, 'x = {b}'.format(b=y_intercept), fontsize=7)
    plt.show()

    # plt.savefig('7_6.png')
