#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = -float("inf")

    for t in range(N):
        max_ap = -float("inf")
        idx = 0
        for a in range(N):
            if a == t: continue

            ap = sum(A[min(a,t)+1:max(a,t)+1:2])
            
            if ap > max_ap:
                idx = a
                max_ap = ap
        
        tp = sum(A[min(idx,t):max(idx,t)+1:2])
        ans = max(ans, tp)

    return ans

print(main())

# self AC
