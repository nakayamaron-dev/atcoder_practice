#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

visited = [-1] * N

def visit(x):
    visited[x] = 1
    s.append(x)
    for nx in g[x]:
        if visited[nx] == -1:
            visit(nx)

def paint(x):
    for nx in g[s[x]]:
        if c[s[x]] == c[nx]:
            return 0

    if x == len(s) - 1:
        return 1

    res = 0
    for i in range(3):
        c[s[x+1]] = i
        res += paint(x+1)
        c[s[x+1]] = -1

    return res

ans = 1
for i in range(N):
    if visited[i] != -1:
        continue

    s = []
    visit(i)

    c = [-1] * N
    c[i] = 0

    ans *= paint(0) * 3

print(ans)

# not self AC
# DFSなのはわかったが、実装がわからなかった。
# とりあえず解答を写したが、理解はできていない。
