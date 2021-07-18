#!/usr/bin/env python3
def main():
    H, W = map(int,input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    col, row = [], []

    for w in range(W):
        tmp = 0
        for a in A:
            tmp += a[w]
        
        col.append(tmp)
    
    for h in range(H):
        row.append(sum(A[h]))
    
    for h in range(H):
        for w in range(W):
            A[h][w] = col[w] + row[h] - A[h][w]
        
        print(*A[h])

main()
