#!/usr/bin/env python3
# 隣接するマスが偶数→表、奇数→裏
def main():
    N, M = map(int,input().split())

    if (N-2)*(M-2) == 0:
        return 0
    elif (N-2)*(M-2) < 0:
        return N*M-2
    else:
        return (N-2)*(M-2)
    
print(main())

# self AC

