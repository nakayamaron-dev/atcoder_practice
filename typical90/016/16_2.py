#!/usr/bin/env python3
def main():
    N = int(input())
    A, B, C = map(int,input().split())

    ans = 10**9 + 7

    for a in range(10000):
        if A*a > N:
            break

        for b in range(10000):

            if A*a + B*b > N:
                break

            k = N - (A*a + B*b)
            if k % C == 0 and k >= 0:
                ans = min(ans, a+b+k//C)
    
    return ans

print(main())