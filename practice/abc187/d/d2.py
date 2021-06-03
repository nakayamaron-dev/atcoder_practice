#!/usr/bin/env python3
def main():
    N = int(input())
    dim = 0
    arr = []

    for _ in range(N):
        A, B = map(int,input().split())
        dim -= A
        arr.append(2*A + B)
    
    arr.sort()
    ans = 0
    while dim <= 0:
        dim += arr.pop()
        ans += 1
    
    return ans

print(main())

# not self AC
# 二人の得点を比較する場合、差分を考えることで一つの指標になりシンプルになることもある。
