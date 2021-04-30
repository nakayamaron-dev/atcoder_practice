#!/usr/bin/env python3
def main():
    n, m = map(int,input().split())
    ks = [list(map(int, input().split())) for _ in range(m)]
    p = list(map(int, input().split()))
    ans = 0

    # ビット全探索
    for bit in range(2**n):
        on = 0
        # 電球全探索
        for i in range(m):
            on_sw = 0
            # スイッチ全探索
            for j in range(1, len(ks[i])):
                if (bit >> ks[i][j]-1) & 1:
                    on_sw += 1
            
            #onのスイッチの数を2で割った余りがp[i]と同じ場合電球がonになる。
            if on_sw % 2 == p[i]:
                on += 1
        
        # onの電球の数がmの場合、条件に当てはまる。
        if on == m:
            ans += 1
    
    return ans

print(main())

# not self AC
# もう一度チャレンジする。

