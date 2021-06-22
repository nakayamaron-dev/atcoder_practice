#!/usr/bin/env python3
def main():
    N = int(input())
    ans = 0

    for i in range(1, N):
        ans += N / (N-i)
    
    return ans

print(main())

# i個選択済みの状態で未選択の頂点を選ぶ確率は(N-i)/N
# 期待値は確率の逆数なので、N / (N-i)
