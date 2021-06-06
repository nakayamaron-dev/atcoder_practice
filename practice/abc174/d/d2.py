#!/usr/bin/env python3
def main():
    N = int(input())
    C = input()
    
    # i番目までの赤石の累積
    cnt = [0]*N
    red = 0

    for i in range(N):
        if C[i] == 'R':
            red += 1

        cnt[i] = red
    
    return red - cnt[red-1]

print(main())

# 赤石の数が4つであれば、左から4つの石を赤石にする必要がある。
# よって左から4つの石の中で白石の数が答えになる。
# これは自力で解きたい問題