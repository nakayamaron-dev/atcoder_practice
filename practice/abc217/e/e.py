#!/usr/bin/env python3
from collections import deque
from heapq import heappush, heappop


def main():
    Q = int(input())
    d = deque()
    h = []

    for _ in range(Q):
        q = list(map(int, input().split()))

        if q[0] == 1:
            d.append(q[1])
        elif q[0] == 2:
            print(heappop(h) if h else d.popleft())
        else:
            while d:
                heappush(h, d.pop())


main()
