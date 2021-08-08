#!/usr/bin/env python3
from bisect import bisect_left,bisect_right
def main():
    H, W, N = map(int,input().split())
    row, col = set(), set()
    cards = []

    for i in range(1, N+1):
        A, B = map(int,input().split())
        A, B = A-1, B-1
        col.add(B)
        row.add(A)
        cards.append((A, B, i))
    
    col = sorted(list(col))
    row = sorted(list(row))
    
    for i in range(N):
        x, y, num = cards[i][1], cards[i][0], cards[i][2]

        ansx = bisect_left(col, x) + 1
        ansy = bisect_left(row, y) + 1

        print(ansy, ansx)

main()

# 座標圧縮らしい。