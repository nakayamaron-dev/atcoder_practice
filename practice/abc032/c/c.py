#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    S = [int(input()) for _ in range(N)]

    if 0 in S: return N
    
    right, now, ans = 0, 1, 0
    
    for i in range(N):
        while right < N and now * S[right] <= K:
            now *= S[right]
            right += 1
        
        ans = max(right-i, ans)
        if right > i:
            now //= S[i]

        if right == N-1:
            break
        
        if right == i:
            right += 1
        
    return ans

print(main())

# not self AC
# 尺取法を勉強する必要あり。
        