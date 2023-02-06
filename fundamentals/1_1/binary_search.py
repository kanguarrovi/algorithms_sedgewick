import sys

def rank(key: int, a: list) -> int:
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo)/2
        if key < a[mid]:
            hi = mid - 1
        elif key > a[mid]:
            lo = mid + 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    whilelist = None
    with open(sys.argv[1]) as f:
        whilelist = list(map(int,[line.rstrip() for line in f]))
    whilelist.sort()
    while not sys.stdin.isatty():
        key = int(input().strip())
        if rank(key, whilelist) == -1:
            print(key)


