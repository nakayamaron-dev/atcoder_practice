#!/usr/bin/env python3
import math
def main():
    N = int(input())
    X0, Y0 = map(int,input().split())
    Xh, Yh = map(int,input().split())
    Xc, Yc = (X0+Xh)/2, (Y0+Yh)/2
    rad = math.radians(360/N)

    # 中心を(0, 0)に並行移動させる。
    X0 -= Xc
    Y0 -= Yc
    Xh -= Xc
    Yh -= Yc

    ansx = X0 * math.cos(rad) - Y0 * math.sin(rad) + Xc
    ansy = X0 * math.sin(rad) + Y0 * math.cos(rad) + Yc

    print(ansx, ansy)

main()

# self AC
# 座標(0, 0)を中心に回転移動させる公式がわかれば簡単。