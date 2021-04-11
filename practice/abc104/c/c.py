#!/usr/bin/env python3
D, G = map(int,input().split())
PC = []
for i in range(D):
    p, c = map(int,input().split())
    PC.append([(i+1)*100, p, c])

ans = 10**9

# 1問も解かないか、全部解くかのビット全探索
for i in range(2**D):
    score = 0
    cnt = 0
    flg = 0
    # 各問題の総得点を計算
    for j in range(D):
        #問題を全て解く場合
        if (i>>j) & 1:
            score+= PC[j][2]+PC[j][1]*PC[j][0]
            cnt += PC[j][1]
        # 問題を解かない場合、その内一番高い番号をメモしておく。
        else:
            flg = j
    
    if score >= G:
        ans = min(ans, cnt)
    else:
        remain_cnt = -(-((G-score)//100)//(flg+1))
        if remain_cnt < PC[flg][1]:
            ans = min(ans, cnt+remain_cnt)

print(ans)

# not self AC
# ポイント：1問も解かないか、全部解くかでよい。点数の低い問題を中途半端に解くくらいであれば、より高得点の問題を解く。
# よって1問も解かないか、全部解くかのビット全探索
