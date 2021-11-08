# 再帰上限を増やす
import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
g = [[] for _ in range(N+1)]
ans = 0


def dfs(v):
    if visited[v]:
        return

    visited[v] = True
    global ans
    ans += 1
    for nv in g[v]:
        dfs(nv)


for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    g[A].append(B)

for i in range(N):
    visited = [False] * (N+1)
    dfs(i)

print(ans)
