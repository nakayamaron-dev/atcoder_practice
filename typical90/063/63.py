#!/usr/bin/env python3
from collections import Counter
def main():
    H, W = map(int,input().split())
    P = [list(map(int, input().split())) for _ in range(H)]
    ans = 0

    for bit in range(2**H):
        cnt = Counter()
        cnt[0] = 0

        for w in range(W):
            check = []
            for h in range(H):
                if (bit >> h) & 1:
                    check.append(P[h][w])
            
            if len(set(check)) == 1:
                cnt[check[0]] += len(check)
        
        ans = max(ans, max(cnt.values()))
    
    return ans

print(main())