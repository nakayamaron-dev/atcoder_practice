#!/usr/bin/env python3
def main():
    H, W = map(int,input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]
    dim = [[0]*W for _ in range(H)]
    cnt = 0

    for h in range(H):
        for w in range(W):
            dim[h][w] = A[h][w] - B[h][w]
    
    for h in range(H-1):
        for w in range(W-1):
            tgt = dim[h][w]
            
            if tgt != 0:
                cnt += abs(tgt)
                for nh, nw in [[h, w], [h+1, w], [h, w+1], [h+1, w+1]]:
                    dim[nh][nw] -= tgt
    
    for itm in dim:
        if sum(itm) != 0:
            print("No")
            exit()
    
    print("Yes")
    print(cnt)

main()