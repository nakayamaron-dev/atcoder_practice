# 全探索だと解けそうだが、TLEになることは明白。

def main():
    N, K = map(int,input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    S = [[0]*801 for _ in range(801)]

    ng = 0
    ok = 10**9 + 1

    lim = int(K*K/2 + 1)

    # 二分探索
    while ng+1 < ok:
        mid = (ng+ok) // 2

        # 2次元配列の累積和を求めておく。
        for i in range(N):
            for j in range(N):
                S[i+1][j+1] = S[i+1][j] + S[i][j+1] - S[i][j]

                if A[i][j] > mid:
                    S[i+1][j+1] += 1

        ext = False
        for i in range(N-K+1):
            for j in range(N-K+1):
                if S[i+K][j+K] + S[i][j] - S[i][j+K] - S[i+K][j] < lim:
                    ext = True
        
        if ext: ok = mid
        else: ng = mid
    
    return ok

print(main())

# not self AC
# 二分探索は思いつかない。
