#!/usr/bin/env python3
def main():
    N = int(input())
    S = input()
    ans = 0

    # 暗証番号1000通り作れるかどうか
    for i in range(1000):
        pwd = str(i).zfill(3)

        minidx = 0
        for s in pwd:
            if s not in S[minidx:]:
                break

            minidx = S[minidx:].index(s) + minidx + 1
        else:
            ans += 1
    
    return ans
    
print(main())

