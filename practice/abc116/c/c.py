#!/usr/bin/env python3
def main():
    N = int(input())
    H = list(map(int, input().split()))
    
    ans = H[0]
    for i in range(1,N):
        ans += max(0, H[i] - H[i-1])
    
    return ans

print(main())

# not self AC
