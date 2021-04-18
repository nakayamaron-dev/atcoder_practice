#!/usr/bin/env python3
def main():
    N, M = map(int,input().split())
    l = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        l[a-1].append(b-1)
        l[b-1].append(a-1)
    
    ans = 0
    while True:
        cnt = 0
        for i in range(N):
            if len(l[i]) == 1:
                l[l[i][0]].remove(i)
                l[i] = []
                cnt += 1
            
        if cnt == 0: break
        ans += cnt
    
    return ans

print(main())

# not self AC
# グラフ形式が苦手
