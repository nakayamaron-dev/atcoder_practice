#!/usr/bin/env python3
# 方針
# 制約条件：1 <= H,W <= 6より、おそらく全探索
H, W, K = map(int,input().split())
C = []
for i in range(H):
    c = input().replace('.','0').replace('#','1')
    c = [int(i) for i in c]
    C.append(c)

ans = 0
for i in range(2**H):
    for j in range(2**W):
        cnt = 0
        for h in range(H):
            for w in range(W):
                # 縦 or 横で選ばれている場合は赤色になる。
                if ((i>>h)&1) or ((j>>w)&1):
                    continue
                # 選ばれてないマスの場合、黒であれば1, 白であれば0を加算
                else:
                    cnt += C[h][w]
            
        #個数チェック
        if cnt == K:
            ans += 1

print(ans)

## not self AC