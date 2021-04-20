#!/usr/bin/env python3
def main():
    SX, SY, TX, TY = map(int,input().split())
    x = TX - SX
    y = TY - SY
    ans = "U"*y + "R"*x + "D"*y + "L"*x
    ans += "L" + "U"*(y+1) + "R"*(x+1) + "DR" + "D"*(y+1) + "L"*(x+1) + "U"

    return ans

print(main())

# self AC
# 変わり種の問題
