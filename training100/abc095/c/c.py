#!/usr/bin/env python3
def main():
    A, B, C, X, Y = map(int,input().split())

    # ABピザ2枚買う方が安い場合
    if C*2 <= A + B:
        # AとB少ない方が揃うようにABピザを買う。
        cost = C * 2 * min(X, Y)

        # 残りはABピザ2枚と単品で買う場合と安い方をTakeする。
        if X <= Y:
            if C*2 <= B:
                cost += C * 2 * (Y - X)
            else:
                cost += B * (Y - X)
        else:
            if C*2 <= A:
                cost += C * 2 * (X - Y)
            else:
                cost += A * (X - Y)
    else:
        # それぞれ単品で購入した方が安い。
        cost = A * X + B * Y
    
    return cost

print(main())
