#!/usr/bin/env python3
def main():
    n = int(input())
    mod = 10**9 + 7
    ans = pow(10, n, mod) - pow(9, n, mod) - pow(9, n, mod) + pow(8, n, mod)
    return ans % mod

print(main())

# self AC
