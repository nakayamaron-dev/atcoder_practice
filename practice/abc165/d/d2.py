#!/usr/bin/env python3
def main():
    A, B, N = map(int,input().split())
    x = min(N, B-1)

    return A*x // B

print(main())

# ある程度手動で計算していくと、計算結果がループしていくことに気づく。
# よって、NとB-1の小さい方をxとして計算したものが答えになる。
