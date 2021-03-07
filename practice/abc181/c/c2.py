# 方針
# 制約がN < 10**2と少ないので、おそらく全探索 (nC3)

#!/usr/bin/env python3
def combinations_array(num_array, r):
    import itertools
    return list(itertools.combinations(num_array, r))

N = int(input())
XY = [list(map(int, input().split())) for l in range(N)]
ans = "No"

for ptn in combinations_array(XY, 3):
    #ある一つの点が原点にくるように平行移動させる。
    point1 = [ptn[1][0] - ptn[0][0], ptn[1][1] - ptn[0][1]]
    point2 = [ptn[2][0] - ptn[0][0], ptn[2][1] - ptn[0][1]]

    #o割りをしないように、y1/x1 == y2/x2 → y1*x2 == y2*x2という形に変換する。
    if point1[0]*point2[1] == point1[1]*point2[0]:
        ans = "Yes"
        break

print(ans)

## self AC
