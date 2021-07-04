#!/usr/bin/env python3
def main():
    N = int(input())
    H, S = [], []
    for _ in range(N):
        h,s = map(int, input().split())
        H.append(h)
        S.append(s)
    
    left, right = 0, 10**18

    while right - left > 1:
        mid = (right + left) // 2
        times = []
        
        #得点midで終えるためにはそれぞれ風船を何秒以内に撃ち落とす必要があるか調べる。
        for i in range(N):
            time = (mid-H[i]) // S[i]
            times.append(time)
        
        # 制限時間以内に撃ち落とせない風船が一つでもあれば条件を満たさない。
        times.sort()
        for idx, itm in enumerate(times):
            if itm < idx:
                left = mid
                break
        else:
            right = mid
    
    return right

print(main())

#得点Sで終えることができるかどうか、二分探索によって求める。