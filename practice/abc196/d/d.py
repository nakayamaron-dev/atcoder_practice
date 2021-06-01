#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10 ** 6)

H, W, A, B = map(int, input().split())
N = H * W

def dfs(i, bit, a, b):
    '''
    i: 現在位置
    bit: 畳の敷設状態を示すビット列
    a, b: 畳の残り枚数
    '''
    ret = 0  # ret: 現在マス以降の敷き方の総数
    h, w = divmod(i, W)  # h, w: 現在マスはh列w行
    if i == H * W:  # 全マスに敷き終わった場合
        ret = 1
    elif (bit >> i) & 1:  # 現在マスが既に敷設済の場合
        ret += dfs(i + 1, bit, a, b)  # 何もせず次のマスに移動
    else:  # 現在マスの畳の敷き方
        # Bを敷く場合
        if b > 0:
            nbit = bit | (1 << i)
            ret += dfs(i + 1, nbit, a, b - 1)
        # Aを横向きに敷く
        if a > 0 and w < W - 1 and not (bit >> (i + 1)) & 1:
            # 横のマス(i + 1)が空いているときのみ可能
            nbit = bit | (1 << i) | (1 << (i + 1))
            ret += dfs(i + 1, nbit, a - 1, b)
        # Aを縦向きに敷く
        if a > 0 and h < H - 1 and not (bit >> (i + W)) & 1:
            # 下のマス(i + W)が空いているときのみ可能
            nbit = bit | (1 << i) | (1 << (i + W))
            ret += dfs(i + 1, nbit, a - 1, b)
    return ret

ans = dfs(0, 0, A, B)

print(ans)

# not self AC