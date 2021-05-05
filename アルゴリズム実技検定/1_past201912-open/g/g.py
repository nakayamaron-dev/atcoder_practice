#!/usr/bin/env python3
def main():
    N = int(input())
    A = []
    for i in range(N-1):
        a = list(map(int, input().split()))
        A.append([0]*(i+1) + a)
    
    ALL = 2**N

    # happy[n]: nで表現される集合をグループにしたときの幸福度
    happy = [0] * ALL

    # nで表現される集合に要素iが含まれるか判定してTrue/Falseを返す関数
    def has_bit(n, i):
        return (n & (1<<i) > 0)
    
    # happyの値を前もって計算
    for n in range(ALL):
        for i in range(N):
            for j in range(i+1, N):
                if has_bit(n, i) and has_bit(n, j):
                    happy[n] += A[i][j]
    
    ans = -float("inf")
    for n1 in range(ALL):
        for n2 in range(ALL):
            
            # n1とn2で重複があれば無視
            if n1 & n2 > 0:
                continue

            # n3を補集合として求めて答えを更新
            n3 = 2**N - 1 - (n1|n2)
            ans = max(ans, happy[n1] + happy[n2] + happy[n3])
    
    return ans

print(main())