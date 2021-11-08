#!/usr/bin/env python3
from collections import deque
import sys
sys.setrecursionlimit(1000000)


def main():
    N = int(input())
    g = [[] for _ in range(N)]
    T = [0] * N
    visited = [False] * N
    ans = 0

    for i in range(N):
        TKA = list(map(int, input().split()))
        T[i] = TKA[0]
        for j in TKA[2:]:
            g[i].append(j-1)

    def dfs(cur):
        # curの問題を訪れた。
        visited[cur] = True

        # curの問題を解くために必要な問題に遷移していく。
        for nxt in g[cur]:
            if visited[nxt] == False:
                dfs(nxt)

    # main
    dfs(N-1)

    # 訪ねた問題であれば、その時間を答えに加算していく。
    for i in range(N):
        if visited[i]:
            ans += T[i]

    return ans


print(main())
