#!/usr/bin/env python3
def main():
    N, D, K = map(int,input().split())
    E = [list(map(int, input().split())) for _ in range(D)]
    
    for _ in range(K):
        S, T = map(int, input().split())
        l, r = S, S
        for i in range(D):
            if E[i][0] <= l <= E[i][1] or E[i][0] <= r <= E[i][1]:
                l = min(l, E[i][0])
                r = max(r, E[i][1])
            if l <= T <= r:
                print(i+1)
                break

main()

# not self AC
# 難しい
