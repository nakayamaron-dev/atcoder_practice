#!/usr/bin/env python3
def kitaiti(n):
    return (n+1) / 2

def main():
    n, k = map(int,input().split())
    p = list(map(int, input().split()))
    maxval = -float("inf")
    maxarr = []

    for i in range(n-k+1):
        if i == 0:
            tgt = sum(p[i:i+k])
        else:
            tgt -= p[i-1]
            tgt += p[i+k-1]

        if tgt > maxval:
            maxval = tgt
            maxarr = p[i:i+k]
    
    ans = 0
    for itm in maxarr:
        ans += kitaiti(itm)
    
    return ans

print(main())

# self AC
