#!/usr/bin/env python3
def main():
    N = int(input())
    S = input()

    # 左端がリーダーの場合、Eの数が答え
    cnt = S[1:].count("E")
    ans = cnt

    for i in range(1, N):
        # Eが出てくる度に答えが1つ減っていく。
        if S[i] == "E":
            cnt -= 1
        
        # リーダーの左隣がWの場合、答えが一つ増えていく。
        if S[i-1] == "W":
            cnt += 1
        
        ans = min(ans, cnt)
    
    return ans

print(main())

# not self AC
# 累積和で解く。
