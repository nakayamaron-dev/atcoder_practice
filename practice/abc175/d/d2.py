N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = -float('inf')
for s in range(N):
    # Step1
    S = []  # 累積和S. ただし, 初項は0ではなく1回目の移動後の得点とする.
    # 1回目の移動
    i = P[s] - 1
    S.append(C[i])
    # 2回目以降の移動. スタート地点に戻ってくるまで繰り返し.
    while i != s:
        i = P[i] - 1
        S.append(S[-1] + C[i])

    # Step2: KとSの長に応じて場合分けして, 得点の最大値を求める.
    # 1周未満しか移動できない場合:
    if K <= len(S):
        score = max(S[:K])
    # 1周以上回ることができるが, ループを1周したときに得点が減る場合:
    elif S[-1] <= 0:
        score = max(S)
    # 1週以上回ることができ, かつループを1週するごとに得点が増える場合:
    else:
        # ループを (K // len(S) - 1)回 廻る場合:
        score1 = S[-1] * (K // len(S) - 1)
        score1 += max(S)
        # ループを (K // len(S))回 廻る場合:
        score2 = S[-1] * (K // len(S))
        r = K % len(S)
        if r != 0:
            score2 += max(0, max(S[:r]))
        # score1 と score2 の大きい方がこの場合の得点の最大値
        score = max(score1, score2)

    ans = max(ans, score)

print(ans)
