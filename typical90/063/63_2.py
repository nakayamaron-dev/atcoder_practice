#!/usr/bin/env python3
from collections import Counter
def main():
    H, W = map(int,input().split())
    P = [list(map(int, input().split())) for _ in range(H)]
    ans = 0

    for bit in range(2**H):
        dic = Counter()

        for w in range(W):
            pool = []
            for h in range(H):
                if (bit >> h) & 1:
                    pool.append(P[h][w])
            
            if len(set(pool)) == 1:
                dic[pool[0]] += len(pool)

        if dic:
            ans = max(ans, max(dic.values()))
    
    return ans

print(main())