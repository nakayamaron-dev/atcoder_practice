#!/usr/bin/env python3
def digit_num(num):
    return len(str(num))

def main():
    a, b, x = map(int,input().split())
    minval = 0
    maxval = 10**9 + 1
    
    while maxval - minval > 1:
        n = (maxval + minval) // 2
        cost = a*n + b*digit_num(n)

        if cost > x:
            maxval = n
        else:
            minval = n
    
    return minval

print(main())

# not self AC
# 惜しかった。
