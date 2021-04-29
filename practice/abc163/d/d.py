#!/usr/bin/env python3
def main():
    n, k = map(int,input().split())
    arr = [i for i in range(n+1)]
    mod = 10**9+7
    u, d, ans = 0, 0, 0

    for i in range(k, n+2):
        if i == n+1:
            ans += 1
        else:
            if i == k:
                u = sum(arr[-k:])
                d = sum(arr[:k])
            else:
                u += arr[-i]
                d += arr[i-1]
            
            ans += u - d + 1
    
    return ans % mod

print(main())

# self AC
# 模範解答はもっとスマートに解いているが、この方法も悪くないのでは。
