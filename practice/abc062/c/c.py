#!/usr/bin/env python3
def main():
    H, W = map(int,input().split())
    ptn = [H//2 + W//3 + 1, H//3 + W//2 + 1, H, W]

    if H*W % 3 == 0:
        ptn += [0]
    
    if H % 2 == 0:
        ptn += [H//2]
    
    if W % 2 == 0:
        ptn += [W//2]
    
    return min(ptn)

print(main())

# not self AC
# 解答みてもいまいち分からない。
