# 方針
# 
N, K = map(int,input().split())
P = list(map(lambda x: int(x) - 1, input().split()))
C = list(map(int,input().split()))

ans = -float("inf")

# 開始地点は全探索
for i in range(N):
    curr = 0
    score = [0]
    start = i

    #開始地点に戻ってくるまで(移動サイクルを探す)
    while P[start] != i:
        start = P[start]
        curr += C[start]
        score.append(curr)
    
    cycle_score = score[-1] + C[i] #最後に移動分の得点を足す必要がある。
    cycle_len = len(score)

    #サイクル中どこで終わればいいか
    for j in range(cycle_len):


        if j <= K and j != 0:
            #何サイクル目か
            cycles = (K - j) // cycle_len

            #1サイクルの得点が0以下の場合は0、0より大きい場合はサイクル得点が加点される。
            point = score[j] + max(0, cycle_score)*cycles
            ans = max(ans, point)

        elif j == 0 and K >= cycle_len:
            point = cycle_score * K // cycle_len
            ans = max(ans, point)

print(ans)

## not self AC     
# 難しい   
