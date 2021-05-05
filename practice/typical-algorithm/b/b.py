#!/usr/bin/env python3
def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])

    ans = 0
    last = 0
    for a, b in AB:
        if last < a:
            ans += 1
            last = b
    
    return ans
    
print(main())

# 区間スケジューリング問題は終了日が早いものから順番に選んでいく
