#!/usr/bin/env python3
def main():
    N = int(input())
    S = input()
    ans = 0

    maru = batu = -1

    # 最後に見たoとxのいちからlの取りうる位置の個数を答えに足していく。
    for r, c in enumerate(S):
        if c == "o":
            ans += batu + 1
            maru = r
        else:
            ans += maru + 1
            batu = r
    
    return ans

print(main())