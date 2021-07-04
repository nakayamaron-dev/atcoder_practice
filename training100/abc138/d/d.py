#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

def main():
    N, Q = map(int,input().split())
    g = [[] for _ in range(N)]
    ans = [0] * N

    for _ in range(N-1):
        a, b = map(int,input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)

    for _ in range(Q):
        p, x = map(int,input().split())
        #選ばれた頂点にも加点されるため、予め加点しておく。
        ans[p-1] += x
    
    def dfs(pre, cur):
        for itm in g[cur]:
            #親頂点以外に対して処理を実行する。
            if itm != pre:
                ans[itm] += ans[cur]
                dfs(cur, itm)
    
    #最初第一引数は存在しないため、-1としておく。    
    dfs(-1, 0)

    return ans
    
print(*main())
    



