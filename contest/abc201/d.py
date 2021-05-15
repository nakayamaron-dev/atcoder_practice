H, W = map(int,input().split())
A = [input() for _ in range(H)]

taka = 0
aoki = 0

for i in range(H):
    cnt = A[i].count("+")
    taka_row = 0
    aoki_row = 0
    if i % 2 == 0:
        for j in range(1, W, 2):
            if A[i][j] == "+":
                taka_row += 1

        if i == 0 and A[i][0] == "+":
            aoki_row += cnt - taka -1
        else:
            aoki_row += cnt - taka
    else:
        for j in range(0, W, 2):
            if A[i][j] == "+":
                taka_row += 1
        aoki_row += cnt - taka
    
    taka += taka_row
    aoki += aoki_row
    
if taka > aoki:
    print("Takahashi")
elif aoki > taka:
    print("Aoki")
else:
    print("Draw")

