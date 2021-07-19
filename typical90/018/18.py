#!/usr/bin/env python3
import math
def main():
    T = int(input())
    L, X, Y = map(int,input().split())
    Q = int(input())
    
    for _ in range(Q):
        E = int(input())

        # 1周の中での位置を計算
        t = E % T

        # t分後の観覧車の場所
        y = - L/2 * math.sin(2 * math.pi * t/T)
        z = (L/2) * (1 - math.cos(2 * math.pi * t/T))

        # 像との距離計算
        d = math.sqrt(pow(Y-y,2) + pow(X,2))

        # 俯角計算
        print(math.degrees(math.atan(z/d)))

main()