#!/usr/bin/env python3
def main():
    N, M = map(int,input().split())
    g = [[] for _ in range(N)]

    for _ in range(M):
        A, B = map(int,input().split())
        g[A-1].append(B-1)
        g[B-1].append(A-1)

    # 再帰処理で判定する。
    def judge(no, vi):
        if len(vi) == N: return 1

        res = 0
        for e in g[no]:
            if e not in vi:
                res += judge(e, vi+[e])
        
        return res
    
    return judge(0, [0])
    
print(main())

# not self AC
# グラフが苦手、再帰処理も苦手
