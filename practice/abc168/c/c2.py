#!/usr/bin/env python3
import math
A, B, H, M = map(int,input().split())

def main():
    long_angle = 6*M
    short_angle = 30*H + ((M / 60) * 30)
    dim_angle = abs(short_angle - long_angle)
    dim_angle_rad = math.radians(dim_angle)

    return math.sqrt(A**2 + B**2 - 2*A*B*math.cos(dim_angle_rad))

print(main())

## self AC