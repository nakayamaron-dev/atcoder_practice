#!/usr/bin/env python3
# 再帰上限を増やす
import sys
sys.setrecursionlimit(1000000)

def main():
    N, M = map(int,input().split())

    edges = [[] for _ in range(N)]
    indeg = [0]*N

    for i in range(M):
        x, y = map(int,input().split())
        edges[x-1].append(y-1)
        indeg[y-1] += 1
    
    #lengh[i]: 頂点iから始まるパスの最大長
    lengh = [0]*N

    # done[i]: lengh[i]がすでに計算済みであることを示すフラグ
    done = [False]*N

    # メモ化再帰の実装
    def rec(i):
        if done[i]:
            return lengh[i]
        
        lengh[i] = 0
        
        for j in edges[i]:
            lengh[i] = max(lengh[i], rec(j)+1)

        # 計算済みフラグを立てて値を返す
        done[i] = True
        return lengh[i]
    
    #始点全てにおいてrecを呼び出す
    for i in range(N):
        if indeg[i] == 0:
            rec(i)
    
    return max(lengh)

print(main())

# not self AC
# この解放は閉路が存在しないから成立する。
# トポロジカルソート：閉路のないグラフにおいて、辺に沿って進むほど値が大きくなるようにN個の頂点に0,1,...N-1の番号を割り当てる
