import math
R, X, Y = map(int,input().split())

XY = math.sqrt(X**2 + Y**2)

if XY < R:
    print(2)
    exit()
else:
    if XY % R == 0:
        ans = int(XY // R)
    else:
        ans = int(XY // R) + 1

print(ans)
