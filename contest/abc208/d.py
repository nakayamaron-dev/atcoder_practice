import heapq
def main():
    N, M = map(int,input().split())
    G = [[] for _ in range(N)]
    ans = 0

    for _ in range(M):
        A, B, C = map(int,input().split())
        G[A-1].append((B-1, C))
    
    time = [-1] * N

    for cnt in range(N):
        Q = []
        points = []
        p = []
        
        heapq.heappush(Q, (0, cnt))
        time[cnt] = 0

        done = [False] * N
        
        while len(Q) > 0:
            t, i = heapq.heappop(Q)

            if done[i]: continue
            done[i] = True

            p.append(i)
            p2 = p.copy()

            for (j, c) in G[i]:
                if time[j] == -1 or time[j] > time[i] + c:
                    time[j] =  time[i] + c
                    heapq.heappush(Q, (time[j], j))
        
            points.append(p2)

        for idx in range(cnt):
            points = [[0]] + points

        for k in range(N):
            for idx, itm in enumerate(time):
                if max(points[idx]) <= k or max(points[idx]) == cnt or max(points[idx]) == idx:
                    ans += itm
    
    return ans


print(main())