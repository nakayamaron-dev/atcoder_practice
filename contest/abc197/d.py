import math

N = int(input())
X0, Y0 = map(int, input().split())
X1, Y1 = map(int, input().split())

#中心座標
xc = (X0 + X1) / 2
yc = (Y0 + Y1) / 2

xv = X0 - xc
yv = Y0 - yc

theta = 2* math.pi / N
xv2 = math.cos(theta) * xv - math.sin(theta) * yv
yv2 = math.sin(theta) * xv + math.cos(theta) * yv

print(xc+xv2 , yc+yv2)

# not self AC