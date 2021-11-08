#!/usr/bin/env python3
import heapq


def main():
    N, M = map(int, input().split())

    # 入ってくる辺の数をカウントするリスト
    cnt = [0]*(N+1)

    # つながっている辺の情報を格納
    g = [[] for _ in range(N+1)]

    for i in range(M):
        A, B = map(int, input().split())
        g[A].append(B)
        cnt[B] += 1

    que = []
    for i in range(1, N+1):
        # 入ってくる辺の数が0の頂点があればキューへ追加
        if cnt[i] == 0:
            que.append(i)

    heapq.heapify(que)
    ans = []

    while len(que) > 0:
        # キューから一番小さい番号のものを取り出す
        now = heapq.heappop(que)
        ans.append(now)

        for to in g[now]:
            # 辺を消す=toに入ってくる辺の数をマイナス1
            cnt[to] -= 1

            # もし入ってくる辺の数が0になったらキューへ追加
            if cnt[to] == 0:
                # キューへ追加
                heapq.heappush(que, to)

    if len(ans) == N:
        print(*ans)
    else:
        print(-1)


main()
