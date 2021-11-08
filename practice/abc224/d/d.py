#!/usr/bin/env python3
from collections import deque


def main():
    M = int(input())

    G = [[] for _ in range(9)]
    for _ in range(M):
        U, V = map(int, input().split())
        U -= 1
        V -= 1
        G[U].append(V)
        G[V].append(U)

    P = list(map(lambda x: int(x) - 1, input().split()))
    aki = list(set(i for i in range(9)) - set(P))[0]
    P = tuple(P + [aki])

    memo = {P: 0}
    que = deque([P])
    while que:
        x = que.popleft()
        for koma in range(9):
            if x[koma] in G[x[8]]:
                x2 = list(x)
                x2[koma], x2[8] = x2[8], x2[koma]
                x2 = tuple(x2)

                if x2 not in memo:
                    memo[x2] = memo[x] + 1
                    que.append(x2)

    goal = tuple(i for i in range(9))
    print(memo[goal] if goal in memo else -1)


main()
