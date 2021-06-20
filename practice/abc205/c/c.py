#!/usr/bin/env python3
def main():
    A, B, C = map(int,input().split())

    # Cは偶数か奇数かだけの判別でよいので、小さい数字にしても問題ない。
    # Cを小さくすることで、普通にpowの計算ができるようになる。
    C = C%2 + 2

    x = pow(A, C)
    y = pow(B, C)

    if x > y: 
        return ">"
    elif x < y: 
        return "<"
    else: 
        return "="

print(main())