#!/usr/bin/env python3
def main():
    N = int(input())
    TXY = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        if i == 0:
            t = TXY[i][0]
            d = TXY[i][1] + TXY[i][2]
        else:
            t = TXY[i][0] - TXY[i-1][0]
            d = abs(TXY[i][1] - TXY[i-1][1]) + abs(TXY[i][2] - TXY[i-1][2])

        if t < d or t % 2 != d % 2:
            return "No"
    
    return "Yes"

print(main())

# self AC
