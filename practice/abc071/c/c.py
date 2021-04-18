#!/usr/bin/env python3
from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = Counter(A)
    cnt_sr = sorted(cnt.items(), key=lambda x:x[0], reverse=True)
    yoko, tate = 0, 0

    for itm in cnt_sr:
        if itm[1] >= 2:
            yoko = itm[0]
            break
    
    for itm in cnt_sr:
        if itm[0] == yoko:
            if itm[1] >= 4:
                tate = itm[0]
                break
            else:
                continue

        if itm[1] >= 2:
            tate = itm[0]
            break
    
    return yoko*tate

print(main())

# self AC
