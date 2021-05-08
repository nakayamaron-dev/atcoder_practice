#!/usr/bin/env python3
def main():
    n = int(input())

    # T[i][j] := iから始まってjで終わる
    T = [[0]*10 for _ in range(10)]

    # 1からnまでの数字の先頭と末尾の数字を全て覚えておく。
    for i in range(1, n+1):
        S = list(str(i))
        T[int(S[0])][int(S[-1])] += 1
    
    ans = 0
    for i in range(1,10):
        for j in range(1,10):
            ans += T[i][j]*T[j][i]
    
    return ans

print(main())

# not self AC

