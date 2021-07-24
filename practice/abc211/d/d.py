from collections import deque
def main():
    N, M = map(int,input().split())
    MOD = 10**9 + 7
    g = [[]*N for _ in range(N)]

    for _ in range(M):
        A, B = map(int,input().split())
        A, B = A-1, B-1
        g[A].append(B)
        g[B].append(A)
    
    # bfs
    q = deque()
    q.append(0)
    dist = [-1] * N
    dist[0] = 0
    cnt = [0] * N
    cnt[0] = 1

    while q:
        v = q.popleft()
        for i in g[v]:
            if dist[i] != -1:
                if dist[i] == dist[v] + 1:
                    cnt[i] += cnt[v]
                    cnt[i] %= MOD
                continue
            else:
                dist[i] = dist[v] + 1
                cnt[i] = cnt[v]
                q.append(i)
    
    return cnt[-1] % MOD

print(main())