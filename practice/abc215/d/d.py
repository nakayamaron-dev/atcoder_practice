#!/usr/bin/env python3
def prime_factorize(n: int) -> list:
    p = []
    while n % 2 == 0:
        p.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            p.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        p.append(n)
    return p


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = [0]*(M+1)

    for a in A:
        p = prime_factorize(a)

        for j in p:
            # M以上の素因数 or 既出の素因数の場合スキップする。
            if j > M or ans[j] != 0:
                continue

            # M以下の素因数の倍数を答えから除外する。
            for k in range(j, M+1)[::j]:
                ans[k] = 1

    # ansの要素が0の数が答えの数となる。
    print(M - sum(ans))

    for i in range(1, M+1):
        if ans[i] == 0:
            print(i)


main()
