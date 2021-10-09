#!/usr/bin/env python3
from itertools import accumulate


def main():
    N, W = map(int, input().split())

    imos = [0] * 200001
    for _ in range(N):
        s, t, p = map(int, input().split())
        imos[s] += p
        imos[t] -= p

    acc = list(accumulate(imos))
    m = max(acc)

    if m > W:
        return "No"
    else:
        return "Yes"


print(main())

# S分にP増え、T分にP減るイベントと考える。
