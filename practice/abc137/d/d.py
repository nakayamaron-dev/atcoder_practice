#!/usr/bin/env python3
from heapq import heappop, heapify, heappush
def main():
    N, M = map(int,input().split())

    c = [[] for _ in range(M)]
    for _ in range(N):
        A, B = map(int,input().split())
        if A <= M:
            c[A-1].append(-B)
    
    q = []
    ans = 0
    heapify(q)

    for i in range(M):
        for j in c[i]:
            heappush(q, j)
        if q:
            ans += heappop(q)
    
    return -ans

print(main())

# not self AC
# heapqを使って貪欲法。
