#!/usr/bin/env python3
import math
def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    mint = min(A, B, C, D, E)
    ans = math.ceil(N/mint) + 4

    return ans

print(main())