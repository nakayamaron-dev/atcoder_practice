#!/usr/bin/env python3
# 方針
# 制約条件が優しいため、数列Aを全探索

# 重複ありで組み合わせをリスト化
def combinations_with_replacement(arr, n):
    import itertools
    return list(itertools.combinations_with_replacement(arr, n))

N, M, Q = map(int,input().split())
ABCD = [list(map(int, input().split())) for l in range(Q)]

base_arr = [i for i in range(1, M+1)]
patterns = combinations_with_replacement(base_arr, N)

ans = 0
for a in patterns:
    val = 0 
    for idx, itm in enumerate(ABCD):
        if a[itm[1]-1] - a[itm[0]-1] == itm[2]:
            val += itm[3]
    
    ans = max(ans, val)

print(ans)

## self AC
