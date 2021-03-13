#!/usr/bin/env python3
# 順列をリスト化
def permutations_array(arr, r):
    import itertools
    return list(itertools.permutations(arr, r))

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

ptn = permutations_array(range(1, N+1), N)

ans = abs(ptn.index(P) - ptn.index(Q))
print(ans)

## self AC
