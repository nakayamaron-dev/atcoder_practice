#!/usr/bin/env python3

def main():
    N = int(input())
    R = [list(map(int, input().split())) for _ in range(N)]
    B = [list(map(int, input().split())) for _ in range(N)]
    R.sort(key=lambda x: x[1], reverse=True)
    B.sort(key=lambda x: x[0])

    ans = 0
    # blueのx軸が小さい順、redのy軸が大きい順に見ていって、最初に条件を満たすペアを見つける。
    # つまり、条件を満たす、一番距離が近いペアを見つけることになる。
    for b in B:
        for r in R:
            if r[0] < b[0] and r[1] < b[1]:
                ans += 1
                R.remove(r)
                break
    return ans

print(main())

# not self AC
