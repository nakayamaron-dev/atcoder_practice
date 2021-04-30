#!/usr/bin/env python3
def get_lm(a: int, b: int):
    import math
    return (a * b) // math.gcd(a, b)

def main():
    a, b, c, d = map(int,input().split())

    tgt_cnt = b - a + 1
    lm = get_lm(c, d)
    
    c_cnt = b // c - (a-1) // c
    d_cnt = b // d - (a-1) // d
    dup_cnt = b // lm - (a-1) // lm

    ans = tgt_cnt - c_cnt - d_cnt + dup_cnt
    return ans

print(main())

# not self AC
#ある区間における約数の数の求め方に戸惑った。
