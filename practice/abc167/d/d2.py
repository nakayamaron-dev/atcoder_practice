#!/usr/bin/env python3
def main():
    N, K = map(int, input().split())
    A = [0] + list(map(int, input().split()))

    # order[i]: 町iに到達したときの総移動回数
    order = [-1] * (N + 1)

    seen = []
    pos = 1

    while order[pos] == -1:
        order[pos] = len(seen)
        seen.append(pos)
        pos = A[pos]

    period = len(seen) - order[pos] # 循環の周期
    m = order[pos] # 循環する地点

    if K < m:
        return seen[m]
    else:
        K = m + (K - m) % period
        return seen[K]

print(main())

# Kの制約条件が10**18なので、順番に処理していてはTLE
# 鳩ノ巣原理により、N回遷移すれば必ずループする。
# 辿った地点を覚えていく方法で解いた解答を複写した。
