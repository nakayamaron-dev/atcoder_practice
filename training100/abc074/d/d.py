#!/usr/bin/env python3
def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if A[i][j] > A[i][k] + A[k][j]:
                    return -1
    
    # ↓道路構造が存在する場合
    for i in range(N):
        for j in range(N):
            ans += A[i][j]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                #直接移動したときと、経由して移動したとき同じ距離であれば対象外なので答えから引く
                if i != k and j != k and A[i][j] == A[i][k] + A[k][j]:
                    ans -= A[i][j]
                    break
    
    # 対称なテーブル構造なので、答えは半分になる。
    return ans // 2

print(main())
    
