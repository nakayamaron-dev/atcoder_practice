#!/usr/bin/env python3
def main():
    x, k, d = map(int,input().split())
    x = abs(x)

    cnt = x // d

    if cnt >= k:
        return x - d*k
    else:
        if (k-cnt) % 2 == 0:
            return abs(x-d*cnt)
        else:
            return abs(x-d*(cnt+1))

print(main())

# self AC
