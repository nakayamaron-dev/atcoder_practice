#!/usr/bin/env python3
def main():
    N, M = map(int,input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(M):
        for j in range(i+1, M):
            score = 0
            for a in A:
                score += max(a[i], a[j])
            
            ans = max(ans, score)
    
    return ans

print(main())
