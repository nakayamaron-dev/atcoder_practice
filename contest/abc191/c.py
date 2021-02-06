h, w = map(int,input().split())
field = [input() for _ in range(h)]

cnt = 0
for i in range(h-1):
    for j in range(w-1):
        cnt += (
            (field[i][j] == '#')
            + (field[i+1][j] == '#')
            + (field[i][j+1] == '#')
            + (field[i+1][j+1] == '#')
        ) % 2
print(cnt)

# 田を見て。#が奇数となるものをカウントする。