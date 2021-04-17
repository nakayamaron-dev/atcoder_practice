#!/usr/bin/env python3
# ビット全探索
def main():
    N = int(input())
    F = [list(map(int, input().split())) for _ in range(N)]
    P = [list(map(int, input().split())) for _ in range(N)]
    ans = -10**9

    for i in range(1, 2**10):
        tmp = 0
        for j in range(N):
            cnt = 0
            for k in range(10):
                if (i >> k) & F[j][k] == 1:
                    cnt += 1
            
            tmp += P[j][cnt]
        
        ans = max(ans, tmp)
    
    return ans
            
print(main())

# not self AC
# 惜しかった。
