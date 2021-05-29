#!/usr/bin/env python3
def main():
    N, M, Q = map(int,input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))

    # 価値が大きい順番にソート
    WV.sort(key=lambda x: x[1], reverse=True)

    for _ in range(Q):
        L, R = map(int,input().split())
        res = 0
        box = sorted(X[:L-1] + X[R:])

        for w, v in WV:
            for i in range(len(box)):
                # 残っている中で価値が一番大きい品物に対して、入れられる箱があれば入れる。(貪欲法的な考え方)
                if box[i] >= w:
                    res += v
                    box = box[:i] + box[i+1:]
                    break
        
        print(res)

main()

# not self AC
# ナップサック問題みたいだが、DPではなく貪欲法の考え方で解ける。
