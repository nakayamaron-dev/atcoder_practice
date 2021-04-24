#!/usr/bin/env python3
def main():
    S = input()
    arr = S.split("+")
    ans = 0

    for itm in arr:
        if "0" not in itm:
            ans += 1
    
    return ans

print(main())

# self AC
