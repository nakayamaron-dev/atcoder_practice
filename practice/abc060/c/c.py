#!/usr/bin/env python3
def main():
    N, T = map(int,input().split())
    t = list(map(int, input().split()))
    ans = 0

    for i in range(N-1):
        dim = t[i+1] - t[i]
        ans += min(T, dim)
    
    return ans + T

print(main())

# self AC
