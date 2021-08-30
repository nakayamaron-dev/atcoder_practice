N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
A.append(0)
ans = 0
cnt = 0

for i in range(N):
    d = A[i] - A[i+1]
    if d * (i+1) + cnt <= K:
        res = d * (A[i] + A[i+1] + 1) // 2  # 総和の公式
        res *= i + 1  # 最大幸福度の乗り物数
        ans += res
        cnt += d * (i+1)
    else:
        d = (K - cnt) // (i+1)  # 同じ高さを(i+1)回ずつ楽しむ
        ans += (d * (A[i] + A[i+1] - d + 1) // 2) * (i+1)
        cnt += d * (i+1)
        ans += (A[i] - d) * (K - cnt)  # 残りのK-cnt回同じ高さを楽しむ(K-cnt<i+1になっている)
        break

print(ans)
