#!/usr/bin/env python3
def main():
    N = int(input())
    A, B, C = map(int,input().split())
    ans = float("inf")

    for i in range(10000):
        for j in range(10000):
            k = N - (i*A + j*B)

            if k % C == 0 and k >= 0:
                ans = min(ans, i + j + k//C)
    
    return ans

print(main())