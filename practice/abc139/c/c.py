#!/usr/bin/env python3
N = int(input())
H = list(map(int, input().split()))

def solve():
    pos = 0
    move_cnt = 0
    max_move_cnt = 0

    while pos < len(H)-1:
        if H[pos] >= H[pos+1]:
            move_cnt += 1
            if move_cnt > max_move_cnt:
                max_move_cnt = move_cnt
        else:
            move_cnt = 0

        pos += 1
    
    return max_move_cnt

print(solve())

## AC