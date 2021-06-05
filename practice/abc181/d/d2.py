#!/usr/bin/env python3
from collections import Counter
def main():
    S = input()
    s_cnt = Counter(S)

    eights = []
    a = 0
    while a < 992:
        a += 8
        eights.append(a)
    
    for itm in eights:
        cnt = Counter(str(itm))
        ok = True
        if len(str(itm)) == 1:
            if S == "8":
                return "Yes"
        elif len(str(itm)) == 2:
            if S == str(itm) or S[::-1] == str(itm):
                return "Yes"
        else:
            for char in str(itm):
                if s_cnt.get(char, 0) - cnt.get(char, 0) < 0:
                    ok = False
                    break
            
            if ok:
                return "Yes"
    
    return "No"
            
print(main())

# 8の倍数は下3桁が8の倍数であればよいので、3桁までの8の倍数を全探索して作れるものがあるかどうかを探す。
# 解き方はどんくさいが、自分で解けた。