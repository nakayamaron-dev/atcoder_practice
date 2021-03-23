#!/usr/bin/env python3
H, W, A, B = map(int,input().split())

# 深さ優先探索dfs(depth-first search)
def dfs(i, b, x, y):
    if i == H*W:
        return 1
    if (B >> i) & 1:
        return dfs(i+1, B, x, y)
    
    res = 0
    if x:
        p, q = i // W, i % W
        if q + 1 < W:
            res += dfs(i+1, b | (1 << (i+1)), x-1, y)
        if p + 1 < H:
            res += dfs(i+1, b | (1 << (i+W)), x-1, y)
    
    if y:
        res += dfs(i+1, b, x, y-1)
    
    return res

print(dfs(0, 0, A, B))