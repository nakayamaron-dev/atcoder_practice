#!/usr/bin/env python3
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    def check(x):
        s = 0
        for a in A:
            s += max(0, a-x+1)

        return s <= K

    def f(x, y):
        return x*(x+1)//2 - y*(y+1)//2

    ok = 2*10**9 + 7
    ng = 0
    while ok - ng > 1:
        mid = (ok+ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid

    s = 0
    cnt = 0
    for a in A:
        s += f(max(a, ok-1), ok-1)
        cnt += max(a-ok+1, 0)

    s += (K-cnt)*(ok-1)
    return s


print(main())
