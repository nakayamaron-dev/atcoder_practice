#!/usr/bin/env python3
def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    if N > 8:
        A = A[:8]
    
    L = [[] for _ in range(200)]
    M = len(A)

    for bit in range(1, 2**M):
        s = 0 #和
        I = [] #選び方

        for i in range(M):
            if (bit >> i) & 1:
                s += A[i]
                I.append(i+1) #出力はi+1
        
        mod = s % 200 #余り
        L[mod].append(I)

    #総和の余りがiの数列が2つ以上あるか探す。
    for i in range(200):
        if len(L[i]) >= 2:
            B = L[i][0]
            C = L[i][1]
            B_out = [len(B)] + B
            C_out = [len(C)] + C
            print("Yes")
            print(*B_out)
            print(*C_out)
            return
    
    print("No")
    return

main()

# 鳩ノ巣原理により、201個以上の配列があれば、必ず総和の余りが一致する数列がある。
# よってN > 8の場合、確実に答えが存在するのでA[:8]だけを抽出しbit全探索する。
