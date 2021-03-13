#!/usr/bin/env python3
L, R = map(int,input().split())

if R - L > 2019:
    print(0)
else:
    if L - R == 0:
        print(L*L % 2019)
    else:
        minval = 10**9
        for i in range(L, R+1):
            for j in range(i+1, R+1):
                val = i*j % 2019
                minval = min(val, minval)

        print(minval)

## self AC

    