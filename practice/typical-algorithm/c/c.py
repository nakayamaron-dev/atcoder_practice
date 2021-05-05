#!/usr/bin/env python3
def has_bit(n, i):
    return (n & (1<<i) > 0)

def main():
    N = int(input())
    A = []
    for i in range(N):
        a = list(map(int, input().split()))
        A.append(a)
    
    ALL = 2**N

    # cost[n][i]: 訪れた都市の集合がnで、最後にいる都市がiであるときのコスト最小値
    cost = [[float("inf")]*N for _ in range(ALL)]
    cost[0][0] = 0

    for n in range(ALL):
        for i in range(N):
            # iからjに異動する遷移を試す。
            for j in range(N):
                # すでに訪問済みか、同じ都市は無視する。
                if has_bit(n, j) or i == j:
                    continue

                cost[n|(1<<j)][j] = min(cost[n|(1<<j)][j], cost[n][i] + A[i][j])
    
    # 全都市を訪問して始点に戻ってくる最小コストが答え
    ans = cost[ALL-1][0]

    return ans

print(main())
