#!/usr/bin/env python3
import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

order = list(itertools.permutations(range(1, n+1), n))

ans = abs(order.index(p) - order.index(q))
print(ans)

## AC
