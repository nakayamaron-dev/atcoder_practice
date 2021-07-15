#!/usr/bin/env python3
def main():
    H, W = map(int,input().split())
    C = [list(map(int,input().split())) for i in range(10)]
    A = [list(map(int,input().split())) for i in range(H)]
    ans = 0

    for k in range(10):
        for i in range(10):
            for j in range(10):
                C[i][j] = min(C[i][j], C[i][k] + C[k][j])
    
    for i in range(H):
        for j in A[i]:
            if j == 1 or j == -1:
                continue

            ans += C[j][1]
    
    return ans

print(main())
