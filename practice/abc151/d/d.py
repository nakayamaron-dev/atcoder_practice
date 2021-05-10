#!/usr/bin/env python3
from collections import deque
def main():
    h, w = map(int,input().split())
    s= [input() for _ in range(h)]    
    ans = -float("inf")
    
    for sy in range(h):
        for sx in range(w):
            q = deque()
            q.append([sy, sx])
            d = [[-1]*w for _ in range(h)]
            d[sy][sx] = 0

            while len(q) > 0:
                i, j = q.popleft()
                
                for i2, j2 in [[i+1, j],[i-1, j],[i, j+1],[i, j-1]]:
                    if not (0 <= i2 < h and 0 <= j2 < w):
                        continue
                    if s[i][j] == "#" or s[i2][j2] == "#":
                        continue
                    if d[i2][j2] == -1:
                        d[i2][j2] = d[i][j] + 1
                        q.append([i2, j2])
            
            for itm in d:
                ans = max(ans, max(itm))
                        
    return ans

print(main())

# not self AC
# 惜しかった。
