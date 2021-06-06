#!/usr/bin/env python3
from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    counter = Counter(A)
    Sum = sum(A)

    for b, c in BC:
        cnt = counter.get(b, 0)
        Sum = Sum - b*cnt + c*cnt
        del counter[b]

        if counter.get(c, 0) == 0:
            counter[c] = cnt
        else:
            counter[c] += cnt
        
        print(Sum)
    
main()