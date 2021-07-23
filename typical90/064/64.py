#!/usr/bin/env python3
def main():
    N, Q = map(int,input().split())
    A = list(map(int, input().split()))

    e = [A[i] - A[i-1] for i in range(1, N)]
    ans = sum([abs(itm) for itm in e])

    for _ in range(Q):
        l, r, v = map(int,input().split())

        if l > 1:
            ans -= abs(e[l-2])
            e[l-2] += v
            ans += abs(e[l-2])
        if r < N:
            ans -= abs(e[r-1])
            e[r-1] -= v
            ans += abs(e[r-1])
        
        print(ans)

main()