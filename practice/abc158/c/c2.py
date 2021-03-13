#!/usr/bin/env python3
A, B = map(int,input().split())

eight_max = 12.5*(A+1)
eight_min = 12.5*A

ten_max = 10*(B+1)
ten_min = 10*B

for i in range(ten_min, ten_max):
    if i >= eight_min and i < eight_max:
        print(i)
        exit()
print(-1)

## self AC
