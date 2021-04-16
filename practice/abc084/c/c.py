#!/usr/bin/env python3
def main():
    N = int(input())
    CSF = [list(map(int, input().split())) for _ in range(N-1)]

    for i in range(N):
        time = 0
        for j in range(i, N-1):
            # 駅がまだ開通していない場合、始発まで待つ。
            if time < CSF[j][1]:
                time = CSF[j][1]
            
            # 駅が開通しており、待ち時間が発生する場合
            elif time % CSF[j][2] != 0:
                time += CSF[j][2] - time % CSF[j][2]
            
            # 電車に乗っている時間を追加
            time += CSF[j][0]
        
        print(time)

main()

# not self AC
# 惜しかった。
