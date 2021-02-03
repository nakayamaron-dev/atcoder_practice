#!/usr/bin/env python3
from functools import reduce
n, m = map(int,input().split())
sc = [list(map(int, input().split())) for l in range(m)]
maxVal = 0
minVal = 0

# 該当する最小値、最大値を求める。
for i in range(n):
    maxVal += 9 * (10**i)
    if i == 0:
        minVal = 0
    else:
        minVal = 10**i

# 制約条件がゆるいため、全県探索で解く。
def main():
    for num in range(minVal, maxVal+1):
        isOk = True
        # 桁配列に変換する。
        digits = [int(x) for x in list(str(num))]
        
        for itm in sc:
            if digits[itm[0]-1] != itm[1]:
                isOk = False
                break
        if isOk == True:
            # 数字に戻す
            ans = int(reduce(lambda x, y: x + y, [str(x) for x in digits]))
            return ans
    
    return -1

print(main())
            
## AC    
    