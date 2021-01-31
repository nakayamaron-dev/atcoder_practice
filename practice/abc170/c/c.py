#!/usr/bin/env python3
x, n = map(int,input().split())
p = list(map(int,input().split()))

def main():
    loop = True
    cnt = 0
    if n == 0:
        return x
    else:
        while loop:
            if x - cnt not in p:
                return x - cnt
            elif x + cnt not in p:
                return x + cnt
            else:
                cnt += 1

print(main())

## AC