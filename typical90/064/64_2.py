#!/usr/bin/env python3
def main():
    N, Q = map(int,input().split())
    A = list(map(int, input().split()))

    # 初期状態のeと不便さを計算しておく。
    e = [A[i] - A[i-1] for i in range(1, N)]
    ans = sum([abs(itm) for itm in e])

    for _ in range(Q):
        l, r, v = map(int,input().split())
        l, r = l-1, r-1

        # 区間[l, r]において中間範囲は不便さは変わらない。
        # 変わるのは最初と最後の項目だけ。
        if l > 0:
            ans -= abs(e[l-1])
            e[l-1] += v
            ans += abs(e[l-1])
        if r < N-1:
            ans -= abs(e[r])
            e[r] -= v
            ans += abs(e[r])
        
        print(ans)

main()