#!/usr/bin/env python3
def main():
    H, W = map(int,input().split())
    C = [input() for _ in range(H)]

    def dfs(h, w, d=0):
        vis[h][w] = True

        if dist[h][w] != -1:
            if d - dist[h][w] < 3:
                return -1
            
            return d - dist[h][w]
        
        res = -1
        dist[h][w] = d
        for dh, dw in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            nh, nw = h+dh, w+dw

            if nh < 0 or nw < 0 or nh >= H or nw >= W or C[nh][nw] == "#":
                continue

            res = max(res, dfs(nh, nw, d+1))
        
        dist[h][w] = -1
        return res

    vis = [[False]*W for _ in range(H)]
    dist = [[-1]*W for _ in range(H)]
    ans = -1

    for h in range(H):
        for w in range(W):
            if vis[h][w] or C[h][w] == "#":
                continue

            ans = max(ans, dfs(h, w))
    
    return ans

print(main())