#!/usr/bin/env python3
def main():
    N, M, Q = map(int,input().split())

    table = [[0]*N for _ in range(N)]
    for _ in range(M):
        L, R = map(int,input().split())
        L, R = L-1, R-1

        for r in range(R, N):
            # Lをスタートした際、終着がRより遠い地点がクエリにあった場合含まれることになるので+1しておく。
            table[L][r] += 1
    
    for _ in range(Q):
        p, q = map(int,input().split())
        p, q = p-1, q-1
        ans = 0

        for s in range(p, q+1):
            # クエリ範囲内の都市それぞれスタートした時の終着q以内に収まる路線の数
            ans += table[s][q]
        
        print(ans)

main()
