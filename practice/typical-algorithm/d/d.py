#!/usr/bin/env python3
import heapq
def main():
    N, M = map(int,input().split())

    #隣接リストとしてグラフを作成
    g = [[] for _ in range(N)]

    for _ in range(M):
         u, v, c = map(int,input().split())

         # uからvへと、重みのcの辺が張られているため、行き先のvだけでなく、重みのcも入れておく
         g[u].append((v, c))
    

    # 頂点0から各頂点への最短距離ほ保持する配列
    dist = [-1] * N

    # ダイクストラ法で使うヒープ
    q = []

    # 始点となる頂点0をヒープに追加しておく
    # (距離, 頂点)として追加
    heapq.heappush(q, (0, 0))

    # 始点となる頂点0への最短距離は0とする。
    dist[0] = 0

    # ヒープから取り出したことがあるかどうか保存する配列
    done = [False] * N

    # ダイクストラ法で各頂点への最短距離を求める
    while len(q) > 0:

        # ヒープの先頭の頂点を取り出してiとする。
        d, i = heapq.heappop(q)

        # もし前にヒープから取り出したことがあれば、隣接する頂点を調べるのをスキップ
        if done[i]: continue

        # ヒープから頂点iを取り出したことを記録
        done[i] = True

        # 頂点iに隣接する頂点を順番に見る
        # 見ている頂点をjとする
        # iからjへ移動するときに使う辺の重みをcとする
        for (j, c) in g[i]:
            # jが未訪問 or jへの最短距離が更新可能 → jへの最短距離を更新してヒープの末尾に追加
            if dist[j] == -1 or dist[j] > dist[i] + c:
                dist[j] = dist[i] + c
                heapq.heappush(q, (dist[j], j))
        
    return dist[N-1]

print(main())

# ダイクストラ法の練習問題
