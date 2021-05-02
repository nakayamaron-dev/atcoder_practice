#!/usr/bin/env python3
import math
def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    mint = min(a,b,c,d,e)
    # 交通機関の中で最小人数しか運べないものに合わせてもかかる時間は同じ。
    ans = math.ceil(n/mint) + 4

    return ans

print(main())

# not self AC
# 考え方はあっていた、再度挑戦。
