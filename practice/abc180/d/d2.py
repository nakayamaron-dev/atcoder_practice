#!/usr/bin/env python3
def main():
    X, Y, A, B = map(int,input().split())
    power = X
    exp = 0

    while power*A < B and A * power < Y:
        power *= A
        exp += 1
        
    exp += (Y - power - 1) // B

    return exp

print(main())    

# A倍とBを足す選択肢で、強さが小さい方を選択する。
# 強さが小さい場合はA倍、あるところからBを足す方が小さくなるので、その分岐点を考えれば良い。
# Bを足す方に移行した後、イテレーションでは時間かかる場合があるので、少し工夫すればOK。
