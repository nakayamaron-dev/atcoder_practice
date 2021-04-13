#!/usr/bin/env python3

#上下左右が全て白色の#が一つでもあればNo, それ以外Yes
#端、角、中の3種類
def main():
    H, W = map(int,input().split())
    S = [ input() for l in range(H)]

    for w in range(W):
        for h in range(H):
            #角4パターン
            if S[h][w] == "#":
                if w == 0 and h == 0:
                    if S[h][w+1] == "." and S[h+1][w] == ".":
                        return "No"
                elif w == W-1 and h == 0:
                    if S[h][w-1] == "." and S[h+1][w] == ".":
                        return "No"
                elif w == 0 and h == H-1:
                    if S[h][w+1] == "." and S[h-1][w] == ".":
                        return "No"
                elif w == W-1 and h == H-1:
                    if S[h][w-1] == "." and S[h-1][w] == ".":
                        return "No"
                #端4パターン
                elif h == 0:
                    if S[h][w-1] == "." and S[h][w+1] == "." and S[h+1][w] == ".":
                        return "No"
                elif h == H-1:
                    if S[h][w-1] == "." and S[h][w+1] == "." and S[h-1][w] == ".":
                        return "No"
                elif w == 0:
                    if S[h+1][w] == "." and S[h-1][w] == "." and S[h][w+1] == ".":
                        return "No"
                elif w == W-1:
                    if S[h+1][w] == "." and S[h-1][w] == "." and S[h][w-1] == ".":
                        return "No"
                else:
                    if S[h+1][w] == "." and S[h-1][w] == "." and S[h][w-1] == "." and S[h][w+1] == ".":
                        return "No"
    
    return "Yes"

print(main())

# self AC
# もっと簡単に実装できるはず。
# 最初に外に1週囲えばよいのでは？            
