# 02 - array of random values

import random
import matplotlib.pyplot as plt

N = 50
a = [random.random() for i in range(N)]
for i in range(N):
    x = 1.0 * i / N
    y = a[i] / 2.0
    rw = 0.5 / N
    rh = a[i] / 2.0
    plt.bar(x, rh, width=rw, bottom=y, color="blue")

plt.show()

