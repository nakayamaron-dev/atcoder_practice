#!/usr/bin/env python3
S = input()

ptn10 = 0
ptn01 = 0

for idx, itm in enumerate(S):
    if idx % 2 == 0:
        if itm == "1":
            ptn01 += 1
        else:
            ptn10 += 1
    else:
        if itm == "0":
            ptn01 += 1
        else:
            ptn10 += 1

print(min(ptn01, ptn10))
    
# self AC
# 超簡単
