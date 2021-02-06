import math
from decimal import Decimal
x, y, r = map(Decimal,input().split())

def cf(center, radius):
    return math.ceil(center-radius), math.floor(center+radius)

ans = 0
left = math.ceil(x-r)
right = math.floor(x+r)

for i in range(left, right+1):
    p = r**2 - (x-i)**2
    q = p.sqrt()
    top = math.floor(y + q)
    bottom = math.ceil(y - q)
    ans += (top - bottom) + 1

print(ans)

## 浮動小数点の誤差エラーになるので、Decimalを使う。