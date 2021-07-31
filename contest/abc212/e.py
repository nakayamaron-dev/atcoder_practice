from collections import deque
def main():
    N, M, K = map(int,input().split())
    g = [[] for _ in range(N)]
    MOD = 998244353

    for _ in range(M):
        U, V = map(int,input().split())
        U, V = U-1, V-1
        g[U].append(V)
        g[V].append(U)

print(main())