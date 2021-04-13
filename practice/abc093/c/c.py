#!/usr/bin/env python3
def main():
    A, B, C = map(int,input().split())
    arr = sorted([A, B, C])
    tgt = 2*arr[2]-arr[0]-arr[1]

    if tgt % 2 != 0:
        return (tgt+1) //2 +1
    else:
        return tgt //2

print(main())

# self AC
