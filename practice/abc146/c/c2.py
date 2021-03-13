#!/usr/bin/env python3
def digit_num(num):
    return len(str(num))

def calc_cost(A, B, N):
    dn = digit_num(N)
    return A*N + B*dn

A, B, X = map(int,input().split())
low = 0
high = 10**9 + 1

#二分探索
while high - low > 1:
    val = (high+low) // 2

    #料金 > 所持金
    if calc_cost(A, B, val) > X:
        high = val
    else:
        low = val

print(low)

## not self AC
