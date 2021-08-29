#!/usr/bin/env python3
def main():
    XY = float(input())
    X = int(XY)
    Y = int((XY - X) * 10)

    if Y <= 2:
        return str(X) + "-"
    if Y <= 6:
        return str(X)
    if Y <= 9:
        return str(X) + "+"


print(main())
