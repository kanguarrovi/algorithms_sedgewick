# 01 - Function values

import math
import matplotlib.pyplot as plt

N = 100
plt.xlim(0, N)
plt.ylim(0, N * N)

for i in range(1, N + 1):
    plt.scatter(i, i, s=1)
    plt.scatter(i, i*i, s=1)
    plt.scatter(i, i * math.log(i), s=1)

plt.show()
