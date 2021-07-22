#!/usr/bin/env python3
def main():
    H, W = map(int,input().split())
    ans = 0

    # 2*2の領域が作れない場合は全てのマスのLEDを光らせることができる。
    if H == 1 or W == 1:
        return H * W

    for h in range(0, H, 2):
        for w in range(0, W, 2):
            ans += 1
    
    return ans

print(main())