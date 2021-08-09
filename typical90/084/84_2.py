#!/usr/bin/env python3
def main():
    N = int(input())
    S = input()
    ans = 0

    maru = batu = -1

    for i in range(N):
        if S[i] == "o":
            # 直近のxより左側であればlをとれる
            ans += batu + 1
            maru = i
        else:
            ans += maru + 1
            batu = i
    
    return ans

print(main())