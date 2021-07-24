#!/usr/bin/env python3
def main():
    N, M = map(int,input().split())
    g = [[]*N for _ in range(N)]
    ans = 0

    for _ in range(M):
        A, B = map(int,input().split())
        g[max(A, B)-1].append(min(A, B)-1)
    
    for itm in g:
        if len(itm) == 1:
            ans += 1
    
    return ans

print(main())