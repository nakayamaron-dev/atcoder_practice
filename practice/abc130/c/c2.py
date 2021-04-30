#!/usr/bin/env python3
def main():
    w, h, x, y = map(int,input().split())
    ans2 = 0
    
    if x == w/2 and y == h/2:
        ans2 = 1
    
    ans1 = w*h / 2

    return " ".join([str(ans1), str(ans2)])

print(main())

# self AC
