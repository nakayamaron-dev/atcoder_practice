#!/usr/bin/env python3
def main():
    X = abs(int(input()))
    pos, cnt = 0, 0

    while pos < X:
        cnt += 1
        pos += cnt
    
    return cnt

print(main())

# not self AC
# 1+2+3+...+t >= Xで、部分集合がXを取れるのであれば、時刻tにたどり着ける。
