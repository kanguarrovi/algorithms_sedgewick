# def gcd(p:int, q:int) -> int:
#    return p if q == 0 else gcd(q, p % q)

def def gcd(p:int, q:int) -> int:
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)


