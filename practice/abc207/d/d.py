#!/usr/bin/env python3
def main():
    N = int(input())
    
    if N == 1:
        return "Yes"
    
    S = [complex(*map(int, input().split())) for _ in range(N)]
    T = [complex(*map(int, input().split())) for _ in range(N)]

    print(S)

    g = sum(S) / N
    S = [x-g for x in S]
    g = sum(T) / N
    T = [x-g for x in T]

    print(sum(S))
    print(S)

    z = max(S, key=abs) #重心にはない点を一つ選択

    for t in T:
        #重心から同じ距離のもの以外回転しても無駄
        if abs(abs(t) - abs(z)) > 1e-6: 
            continue

        for s in S:
            for u in T:
                #角度が一致した場合
                if abs(s*t - u*z) < 1e-6:
                    break
            else: 
                break
        else:
            return "Yes"
    
    return "No"

print(main())