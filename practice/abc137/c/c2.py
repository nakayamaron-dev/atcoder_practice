#!/usr/bin/env python3
from collections import Counter
def main():
    n = int(input())
    ans = 0
    cache = dict()

    for _ in range(n):
        w = "".join(sorted(input()))

        if cache.get(w, 0) == 0:
            cache[w] = 1
        else:
            ans += cache.get(w, 0)
            cache[w] += 1
    
    return ans

print(main())

# not self AC
