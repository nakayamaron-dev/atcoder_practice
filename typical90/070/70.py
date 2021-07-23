#!/usr/bin/env python3
def main():
    N = int(input())
    ans = 0
    X, Y, XY = [], [], []

    for _ in range(N):
        x, y = map(int,input().split())
        X.append(x)
        Y.append(y)
        XY.append([x, y])
    
    X.sort()
    Y.sort()
    point = [X[N//2], Y[N//2]]

    for x, y in XY:
        ans += abs(point[0] - x) + abs(point[1] - y)
    
    return ans

print(main())