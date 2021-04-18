#!/usr/bin/env python3
def get_lm(a: int, b: int):
    import math
    return (a * b) // math.gcd(a, b)

def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    ans = 1

    for i in range(N):
        ans = get_lm(ans, T[i])

    return ans

print(main())

# self AC
