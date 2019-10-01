import matplotlib.pyplot as plt
import numpy as np
from random import randint
from math import sqrt


def draw_plot(set_len, min_val, max_val):

    point = tuple([randint(min_val, max_val), randint(min_val, max_val)])
    data_set = [(randint(min_val, max_val), randint(min_val, max_val)) for _ in range(set_len)]

    fig = plt.figure()
    ax = fig.add_subplot(111)

    X = [k[0] for k in data_set]
    Y = [k[1] for k in data_set]

    plt.plot(*point, 'ro')
    plt.plot(X, Y, 'b.')

    # anotations: (skipped not needed)
    # for xy in zip(X, Y):
    #     ax.annotate('{},{}'.format(*xy), xy=xy)
    ax.annotate('{}, {}'.format(*point), xy=point)

    # format
    plt.axis([min_val * 1.1, max_val * 1.1, min_val * 1.1, max_val * 1.1])


    # And a corresponding grid
    major_ticks = np.arange(min_val * 1.1, max_val * 1.1, 20)
    minor_ticks = np.arange(min_val * 1.1, max_val * 1.1, 5)
    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

    result = nearest_plot(point, data_set)
    closest = result[0]

    plt.plot(*closest, 'bo', )
    ax.annotate('{}, {}'.format(*closest), xy=closest)


    FMT = 'point:{}\nclosest{}\ndistance:~{:.4}'
    textstr = FMT.format(point, *result)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.01, 0.98, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=props)

    plt.show()


def nearest_plot(origin, dataset):

    def _eu_d(p1, p2):
        d = sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        return d

    min_d = (0, _eu_d(origin, dataset[0]))

    for i, v in enumerate(dataset[1:]):
        dis = _eu_d(origin, v)

        if dis < min_d[1]:
            min_d = (v, dis)

    return min_d


draw_plot(10, -100, 100)

#  todo: doesn't work if result more than 1
