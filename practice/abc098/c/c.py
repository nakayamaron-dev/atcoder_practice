#!/usr/bin/env python3
N = int(input())
S = input()

# リーダーが左端の場合の答え
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

print(ans)

# not self AC
