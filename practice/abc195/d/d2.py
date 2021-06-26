#!/usr/bin/env python3
def main():
    N, M, Q = map(int,input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))

    # 価値が大きい順番にソート
    WV.sort(key=lambda x: x[1], reverse=True)

    for _ in range(Q):
        L, R = map(int,input().split())
        box = X[:L-1] + X[R:]
        box.sort()
        ans = 0

        for w, v in WV:
            for i in range(len(box)):
                if box[i] >= w:
                    ans += v

                    # 箱に2つ品物は入らないので、使った箱は削除する。
                    box = box[:i] + box[i+1:]
                    break
    
        print(ans)

main()