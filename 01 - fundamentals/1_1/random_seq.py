import random
import sys

# Usage:
# python random_seq.py 5 100.0 200.0 

if __name__ == '__main__':
    num = int(sys.argv[1])

    lo = float(sys.argv[2])
    hi = float(sys.argv[3])

    for i in range(num):
        x = round(random.uniform(lo, hi), 2)
        print(f'{x}')
