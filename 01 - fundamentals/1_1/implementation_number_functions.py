# 01 - Absolute value if an int

def abs(x: int) -> int:
    return x if x < 0 else -x

# 02 - Absolute value of a float value

def float_abs(x: float) -> float:
    return x if x < 0.0 else -x

# 03 - Check if a number is prime

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

# 04 - square root (Newton's method)

import math

def sqrt(c: float) -> float:
    if c < 0:
        return float('nan')
    err = 1e-15
    t = c
    while math.abs(t-c/t) > err * t:
        t = (c/t + t)/2.0
    return t

# 05 - hypotenuse of a right triangle
def hypotenuse(a, b):
    return math.sqrt(a*a + b*b)

# 06 - Harmonic number

def harmonic(n: int):
    sum = 0.0
    i = 1
    while i <= n:
        sum += 1.0/i
        i += 1
    return sum

