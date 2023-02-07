import random

# 01 - random float value in [a, b]
def float_uniform(a: float, b: float) -> float:
    return a + random.random() * (b-a)

# 02 - random int value in [0, N]
def int_uniform(num: int) -> int:
    return int(random.random() * num)

# 03 - random int value [lo..hi]
def int_uniform(lo: int, hi:int) -> int:
    return lo + random.uniform(hi - lo)

# 04 - random int value drawn from discrete distribution (i with probabily a[i])
def discrete(a: list):
    # Entries in a[] must sum to 1.
    r = random.random()
    sum = 0.0
    a_length = len(a)
    for i in range(0, a_length):
        sum += a[i]
        if sum >= r:
            return i
    return -1

# 05 - randomly shuffle the elemements in a list of float values
def shuffle(a: list):
    a_length = len(a)
    for i in range(0, a_length):
        r = i + random.uniform(a_length-1)
        temp = a[i]
        a[i] = a[r]
        a[r]= temp
