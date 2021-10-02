#!/usr/bin/env python3

def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    S = [[0]*801 for _ in range(801)]

    ng = -1
    ok = 10**9
    lim = int(K*K/2 + 1)

    while ok - ng > 1:
        mid = (ng+ok) // 2
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

        if ext:
            ok = mid
        else:
            ng = mid

    return ok


print(main())

# not self AC
# 全探索だと解けそうだが、TLEになることは明白。
# 二分探索は思いつかない。
