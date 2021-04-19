#!/usr/bin/env python3
def main():
    S, C = map(int,input().split())
    tmp = C - 2*S
    ans = min(S, C//2) + max(tmp//4, 0)

    return ans

print(main())

# self AC
