def main():
    N = int(input())
    TLR = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    m = 0.001

    for i in range(N):
        for j in range(i+1, N):
            if TLR[i][0] == 1:
                tgt1 = [TLR[i][1], TLR[i][2]]
            elif TLR[i][0] == 2:
                tgt1 = [TLR[i][1], TLR[i][2]-m]
            elif TLR[i][0] == 3:
                tgt1 = [TLR[i][1]+m, TLR[i][2]]
            elif TLR[i][0] == 4:
                tgt1 = [TLR[i][1]+m, TLR[i][2]-m]
            
            if TLR[j][0] == 1:
                tgt2 = [TLR[j][1], TLR[j][2]]
            elif TLR[j][0] == 2:
                tgt2 = [TLR[j][1], TLR[j][2]-m]
            elif TLR[j][0] == 3:
                tgt2 = [TLR[j][1]+m, TLR[j][2]]
            elif TLR[j][0] == 4:
                tgt2 = [TLR[j][1]+m, TLR[j][2]-m]
            
            # 重複チェック
            if tgt1[1] < tgt2[0] or tgt2[1] < tgt1[0]:
                continue
            else:
                ans += 1
    
    return ans

print(main())