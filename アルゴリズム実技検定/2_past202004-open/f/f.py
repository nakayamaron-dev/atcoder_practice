#!/usr/bin/env python3
def main():
    N = int(input())

    T = [[] for _ in range(N)]
    for _ in range(N):
        a, b = map(int,input().split())
        T[a-1].append(b)

    # cnt[n]: 実行可能なタスクの中でポイントがnであるもの
    cnt = [0]*101
    ans = 0

    # N日間ループ
    for d in range(N):
        #d日目から実行可能になるタスクをcntに追加
        for x in T[d]:
            cnt[x] += 1
        
        # cnt[x] > 0である最大のbを探して加算
        # ポイント高い順にループして、0以上が見つかったらbreak
        for x in range(100, 0, -1):
            if cnt[x] > 0:
                ans += x
                cnt[x] -= 1
                break
    
        print(ans)

main()
            


