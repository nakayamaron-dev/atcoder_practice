#!/usr/bin/env python3
def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    cache = dict()

    for a in A:
        if cache.get(a, "None") == "None":
            cache[a] = 1
        else:
            del cache[a]
    
    ans = 0
    for val in cache.values():
        if val == 1:
            ans += 1
    
    return ans

print(main())

# self AC
