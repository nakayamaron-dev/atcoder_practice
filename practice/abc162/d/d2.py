#!/usr/bin/env python3
def main():
    N = int(input())
    S = input()
    ans = 0
    remove = 0
    all_ptn = S.count("R") * S.count("G") * S.count("B")

    for i in range(N):
        for j in range(i+1, N):
            k = j + (j-i)

            if k >= N:
                continue

            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                remove += 1
            
    ans = all_ptn - remove

    return ans

print(main())

# 1つめの条件RGBの選び方はそれぞれの個数をr,g,bとするとr*g*bパターン
# 上記のうち、2つめの条件に当てはまらないものを除外すれば良い。
