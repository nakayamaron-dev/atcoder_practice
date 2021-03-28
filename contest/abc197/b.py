H,W,X,Y = map(int,input().split())
S = [input() for _ in range(H)]

ans = 1
loop = True
row = S[X-1]
col = [s[Y-1] for s in S]

cnt = Y-2
while cnt >= 0:
    if row[cnt] == "#":
        break
    else:
        ans += 1
    cnt -= 1

cnt = Y
while cnt < W:
    if row[cnt] == "#":
        break
    else:
        ans += 1
    cnt += 1

cnt = X-2
while cnt >= 0:
    if col[cnt] == "#":
        break
    else:
        ans += 1
    cnt -= 1

cnt = X
while cnt < H:
    if col[cnt] == "#":
        break
    else:
        ans += 1
    cnt += 1

print(ans)
