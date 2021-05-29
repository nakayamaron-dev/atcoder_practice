#!/usr/bin/env python3
def lm(a: int, b: int):
    import math
    return (a * b) // math.gcd(a, b)

# B以下の倍数 - A以下の倍数
def main():
    A, B, C, D = map(int,input().split())
    CD = lm(C, D)
    div_c = B // C - (A-1) // C
    div_d = B // D - (A-1) // D
    div_cd = B // CD - (A-1) // CD
    
    div = div_c + div_d - div_cd
    
    return (B - A + 1) - div

print(main())
    
# self AC
