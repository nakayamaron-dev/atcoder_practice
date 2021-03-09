#!/usr/bin/env python3
X, N = map(int,input().split())
P = sorted(list(map(int, input().split())))

def main():
    loop = True
    cnt = 0
    if N == 0:
        return X
    else:
        while loop:
            if X-cnt not in P:
                return X-cnt
            elif X+cnt not in P:
                return X+cnt
            else:
                cnt += 1

print(main())

## not self AC
