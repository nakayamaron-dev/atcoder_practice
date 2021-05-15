#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

def main():
    N, Q = map(int,input().split())
    c = [[] for _ in range(N)]
    ans = [0]*N

    for _ in range(N-1):
        A, B = map(int,input().split())
        c[A-1].append(B-1)
        c[B-1].append(A-1)
    
    for i in range(Q):
        P, X = map(int,input().split())
        ans[P-1] += X
    
    def dfs(pre, cur):
        for i in c[cur]:
            if i != pre:
                ans[i] += ans[cur]
                dfs(cur, i)
    
    dfs(-1, 0)
    return " ".join([str(itm) for itm in ans])

print(main())

# not self AC
# dfs、もう少しで解けそうだった。
