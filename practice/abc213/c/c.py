#!/usr/bin/env python3
def compress(arr):
  return {e: i for i, e in enumerate(sorted(set(arr)))}

def main():
    H, W, N = map(int,input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    # 軸毎に座標圧縮
    A = compress([a for a, _ in AB])
    B = compress([b for _, b in AB])

    for a, b in AB:
        print(A[a]+1, B[b]+1)

main()