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
    
    def bfs(x):
        q = deque()
        q.append(x)
        dist = [-1] * N
        dist[x] = 0
        ans = [0] * N
        ans[0] = 1

        while q:
            v = q.popleft()
            for i in g[v]:
                if dist[i] != -1:
                    if dist[i] == dist[v] + 1:
                        ans[i] += ans[v]
                        ans[i] %= MOD
                    continue
                else:
                    dist[i] = dist[v] + 1
                    ans[i] = ans[v]
                    q.append(i)
        
        return ans
    
    ans = bfs(0)
    
    return ans[-1] % MOD

print(main())