#!/usr/bin/env python3
def main():
    N = int(input())
    keta = len(str(N))
    ans = 0

    if keta < 4:
        return 0
    
    for i in range(4, keta+1):
        comma = (i-1) // 3
        start = 10**(i-1)

        if i == keta:
            ans +=((N-start) + 1) * comma
        else:
            ans += 9 * start * comma
    
    return ans

print(main())

# self AC
