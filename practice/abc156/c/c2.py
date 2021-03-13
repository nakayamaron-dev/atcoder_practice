#!/usr/bin/env python3
N = int(input())
X = list(map(int, input().split()))

def main():
    ans = 10**9
    for i in range(1,101):
        dist = 0
        for x in X:
            dist += (i-x)**2
        
        ans = min(ans, dist)
    return ans

print(main())

## self AC
