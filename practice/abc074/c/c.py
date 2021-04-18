#!/usr/bin/env python3
def main():
    A, B, C, D, E, F = map(int,input().split())
    water = set()
    sugar = set()

    for i in range(3001):
        for j in range(3001):
            if 100 * (A*i + B*j) <= F:
                water.add(A*i + B*j)
            if C*i + D*j <= F:
                sugar.add(C*i + D*j)
    
    x, y = 1, 0
    for w in water:
        for s in sugar:
            if 100*w + s <= F and s <= E*w and x*s >= w*y:
                x, y = w, s
    
    print(100*x + y, y)

main()

# not self AC
# 難しい。
