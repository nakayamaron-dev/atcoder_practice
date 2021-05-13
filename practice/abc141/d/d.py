#!/usr/bin/env python3
from heapq import heappop, heapify, heappush
def main():
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    A = [-x for x in A]

    heapify(A)
    for i in range(M):
        itm = - heappop(A)
        heappush(A, -(itm//2))
    
    return sum(A) * -1
        
print(main())

# not self AC
#heapqの使い方を学んだ。
