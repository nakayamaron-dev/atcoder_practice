#!/usr/bin/env python3
def main():
    import math
    n, m = map(int,input().split())
    a = list(map(int, input().split()))
    a2 = [x//2 for x in a]

    l2 = 1
    for itm in a2:
        l2 = l2 * itm // math.gcd(l2, itm)
        if (l2//itm) % 2 == 0:
            return 0
        
    return -(-(m//l2)//2)

print(main())

# not self AC
# 解説見てもわからない。
