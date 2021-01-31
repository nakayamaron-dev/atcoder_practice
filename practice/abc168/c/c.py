#!/usr/bin/env python3
import math
a, b, h, m = map(int,input().split())

def minute_angle():
    if m == 60:
        return 0
    else:
        return 30 * (m / 60)

if m == 0:
    m = 60

if h == 0:
    h = 12

long_angle = 360 * (m / 60)
short_angle = 360 * (h / 12) + minute_angle()

angle = math.radians(abs(long_angle - short_angle))
ans = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle))
print('{:.20f}'.format(ans))

## AC
