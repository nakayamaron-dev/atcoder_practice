#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    cnt, ans = 0, 0
    while ans < K:
        ans += AB[cnt][1]
        cnt += 1

    return AB[cnt-1][0]

print(main())

# self AC
