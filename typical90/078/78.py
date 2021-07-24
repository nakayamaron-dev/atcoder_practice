#!/usr/bin/env python3
def main():
    N, M = map(int,input().split())
    g = [[]*N for _ in range(N)]
    ans = 0

    for _ in range(M):
        A, B = map(int,input().split())
        A, B = A-1, B-1
        Min = min(A, B)
        Max = max(A, B)
        g[Max].append(Min)
    
    for itm in g:
        if len(itm) == 1:
            ans += len(itm)
    
    return ans

print(main())