#!/usr/bin/env python3
def main():
    N, M = map(int,input().split())
    XY = [list(map(int, input().split())) for _ in range(M)]
    ans = 0

    for bit in range(2**N):
        friends = []
        ok = True

        for j in range(N):
            if (bit >> j) & 1:
                friends.append(j+1)

        l = len(friends)
        # 派閥内の人間が全員友達かどうか全組み合わせを試す。
        for x in range(l - 1):
            for y in range(x+1, l):
                if [friends[x], friends[y]] not in XY:
                    ok = False
        
        if ok:
            ans = max(ans, l)
    
    return ans

print(main())
