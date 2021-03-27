#!/usr/bin/env python3
W, H, X, Y = map(int,input().split())

area = W*H / 2
half_w = W / 2
half_h = H / 2

if half_w == X and half_h == Y:
    print(area, 1)
else:
    print(area, 0)

# not self AC
