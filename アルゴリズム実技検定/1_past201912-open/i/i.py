#!/usr/bin/env python3
def main():
    N, M = map(int,input().split())
    S = [0]
    C = [0]
    for _ in range(M):
        s, c = input().split()
        s_val = 0

        for j in range(N):
            if s[j] == "Y":
                s_val |= 1 << j

        S.append(s_val)
        C.append(int(c))
    
    ALL = 2**N

    # cost[i][n]: セットiまで見て揃った部品の集合がnであるときのコスト最小値
    cost = [[float("inf")]*ALL for _ in range(M+1)]
    cost[0][0] = 0

    for i in range(1, M+1):
        for n in range(ALL):
            #セットiを買わない。
            cost[i][n] = min(cost[i][n], cost[i-1][n])

            # セットiを買う。
            cost[i][n|S[i]] = min(cost[i][n|S[i]], cost[i-1][n] + C[i])
    
    # 答えは部品が全部揃っている状態の最小コスト
    # ただし、INFのままなら、部品に揃えることは不可能
    ans = cost[M][ALL-1]
    if ans == float("inf"):
        return -1
    else:
        return ans

print(main())