#!/usr/bin/env python3
def main(flg):
    acm, ans = 0, 0
    for i in range(N):
        acm += A[i]
        if i % 2 == flg and acm <= 0:
            ans += abs(acm-1)
            acm = 1
        if i % 2 != flg and acm >= 0:
            ans += abs(acm+1)
            acm = -1
    
    return ans

N = int(input())
A = list(map(int, input().split()))
print(min(main(0), main(1)))

# not self AC
# ちょっと難しい。
