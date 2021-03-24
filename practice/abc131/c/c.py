#!/usr/bin/env python3
def calc_lm(a: int, b: int):
    import math
    return int(a * b / math.gcd(a, b))

A, B, C, D = map(int,input().split())
CD = calc_lm(C, D)

C_count = B//C - (A-1)//C
D_count = B//D - (A-1)//D
CD_count = B//CD - (A-1)//CD
 
print((B-A+1) - C_count - D_count + CD_count)

# not self AC
