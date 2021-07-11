from collections import deque
def main():
    N, Q = map(int,input().split())
    g = [[] for _ in range(N)]

    for _ in range(N-1):
        A, B = map(int,input().split())
        A -= 1
        B -= 1
        g[A].append(B)
        g[B].append(A)
    
    for _ in range(Q):
        C, D = map(int,input().split())
        C -= 1
        D -= 1

        q = deque()
        q.append(C)
        dist = [-1]*N
        dist[C] = 0
        cnt = 0

        while q:
            cnt += 1
            now = q.popleft()

            if D in g[now]:
                dist[D] = dist[now]+1
                break

            for nxt in g[now]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[now]+1
                    q.append(nxt)
        
        if dist[D] % 2 == 0:
            print("Town")
        else:
            print("Road")

main()

# cからdに向かうときに何個の頂点を通る必要があるかを調べればよい
# 偶数であればRoad, 奇数であればTown