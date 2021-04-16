#!/usr/bin/env python3

def main():
    N, Y = map(int,input().split())
    max_x = min(Y // 10000, N)
    max_y = min(Y // 5000, N)

    for x in range(max_x+1):
        for y in range(max_y+1-x):
            z = N - (x+y)
            if 10000*x + 5000*y + 1000*z == Y:
                print(x, y, z)
                return
    
    print(-1, -1, -1)
    
main()

# self AC
