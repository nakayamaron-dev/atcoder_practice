#!/usr/bin/env python3
N = int(input())

XYH = []
for i in range(N):
    x, y, h = map(int, input().split())
    if h == 0:
        continue
    else:
        XYH.append([x,y,h])

if len(XYH) == 1:
    print(XYH[0][0], XYH[0][1], XYH[0][2])
    exit()

for cx in range(101):
    for cy in range(101):
        ch = []
        for x,y,h in XYH:
            ch.append(abs(cx-x) + abs(cy-y) + h)
        
        ch = list(set(ch))

        if len(ch) == 1:
            print(cx, cy, ch[0])

# not self AC
