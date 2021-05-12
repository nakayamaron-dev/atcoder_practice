#!/usr/bin/env python3
import math
def main():
    a, b, x = map(int,input().split())

    # 平面で考えるための処理。
    x /= a

    if x >= a*b/2:
        t = 2*(a*b-x) / a
        return math.degrees(math.atan(t/a))
    else:
        t = 2*x / b
        return math.degrees(math.atan(b/t))
    
print(main())

# not self AC
# arctanの勉強
