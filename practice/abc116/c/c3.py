#!/usr/bin/env python3
def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = H[0]

    for i in range(1, N):
        if H[i] - H[i-1] > 0:
            ans += H[i] - H[i-1]
    
    return ans

print(main())