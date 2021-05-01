#!/usr/bin/env python3
def main():
    k = int(input())
    tgt = 0
    cnt = 0
    cache = set()
    if k%2 == 0:
        return -1

    while True:
        tgt = (10*tgt + 7) % k

        if tgt == 0:
            return cnt+1

        if tgt in cache:
            return -1
        else:
            cache.add(tgt)
        
        cnt += 1

print(main())

# self AC
