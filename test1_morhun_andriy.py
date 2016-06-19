import numpy as np
a = np.random.random_integers(0, 9, 1000).reshape(10, 10, 10)  # creating of 3d matrix


def coordinates(a):
    x = np.sum(a, axis=0)  # func for sum all numbers for some axis
    y = np.sum(a, axis=1)
    z = np.sum(a, axis=2)
    print(x)  # printing all sums
    print(y)
    print(z)
    x_max = np.amax(x)  # finding position biggest of it
    y_max = np.amax(y)
    z_max = np.amax(z)

    ax0 = np.argwhere(x == x_max)[0]  # calculatind position
    ax1 = np.argwhere(y == y_max)[0]
    ax2 = np.argwhere(z == z_max)[0]

    print("coordinates of biggest axis0 sum are {}, sum is {}".format(ax0, x_max))
    print("coordinates of biggest axis1 sum are {}, sum is {}".format(ax1, y_max))
    print("coordinates of biggest axis2 sum are {}, sum is {}".format(ax2, z_max))
coordinates(a)
