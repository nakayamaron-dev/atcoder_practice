#!/usr/bin/env python3
def iter_product(arr, n):
    import itertools
    return list(itertools.product(arr, repeat=n))

def main():
    n = int(input())
    XY = []
    for _ in range(n):
        a = int(input())
        xy = [list(map(int, input().split())) for _ in range(a)]
        XY.append(xy)
    
    ans = 0
    for ptn in iter_product([0,1], n):
        flag = True
        for i in range(n):
            for x, y in XY[i]:
                if ptn[i] == 1:
                    if ptn[x-1] != y:
                        flag = False
                        break
            
        if flag:
            ans = max(ans, sum(ptn))
    
    return ans

print(main())

# self AC
