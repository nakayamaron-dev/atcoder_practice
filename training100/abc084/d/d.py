#!/usr/bin/env python3
def divi(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    
    divisors.sort()
    return divisors

def main():
    Q = int(input())
    c = [0] * (10 ** 5+1)

    # 予め制約上限まで素数の数を計算しておく。
    for i in range(1, 10**5+1):

        # 累積個数で管理
        c[i] = c[i-1]
        t = divi(i)
        p = divi((i+1)//2)

        # 両方素数であればカウント追加する。
        if len(t) == 2 and len(p) == 2:
            c[i] += 1

    for _ in range(Q):
        L, R = map(int,input().split())

        print(c[R] - c[L-1])

main()
