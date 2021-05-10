#!/usr/bin/env python3
import sys
from collections import deque
sys.setrecursionlimit(pow(10, 6))

def main():
    N = int(input())
    edges = [[] for _ in range(N)]

    for i in range(N-1):
        a, b = map(int,input().split())
        edges[a-1].append((b-1, i))
        edges[b-1].append((a-1, i))
    
    c_num = max(len(edges[i]) for i in range(N))
    ans = [-1] * (N-1)

    def rec(i, p):
        col = []

        for e, ei in edges[i]:
            if ans[ei] != -1:
                col.append(ans[ei])
        
        col.sort()
        col = deque(col)

        ci = 1

        for e, ei in edges[i]:
            if ans[ei] == -1:
                while len(col) > 0 and ci == col[0]:
                    ci += 1
                    col.popleft()
                
                ans[ei] = ci
                ci += 1
            
            if e != p:
                rec(e, i)
    rec(0, -1)

    print(c_num)
    print(*ans, sep='\n')

main()

# not self AC
# まだ途中
