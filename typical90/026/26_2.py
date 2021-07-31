#!/usr/bin/env python3
from collections import deque 
def main():
    N = int(input())
    g = [[] for _ in range(N)]
    
    for _ in range(N-1):
        A, B = map(int,input().split())
        A, B = A-1, B-1
        g[A].append(B)
        g[B].append(A)
    
    colors = [-1] * N
    colors[0] = 0
    q = deque()
    q.append(0)

    while q:
        v = q.popleft()

        for nv in g[v]:
            if colors[nv] != -1:
                continue

            colors[nv] = not colors[v]
            q.append(nv)
    
    zero, one = [], []
    for idx, itm in enumerate(colors):
        if itm == 0:
            zero.append(idx+1)
        else:
            one.append(idx+1)
        
        if len(zero) == N//2:
            return zero
        
        if len(one) == N//2:
            return one

print(*main())
