#!/usr/bin/env python3
def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    MOD = 10**9 + 7

    ans = [[0]*6 for _ in range(N)]

    for i in range(N):
        if i == 0:
            ans[i] = A[i]
        else:
            ans[i] = [x*sum(A[i])%MOD for x in ans[i-1]]

    return sum(ans[-1]) % MOD

print(main())
