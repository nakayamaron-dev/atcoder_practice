#!/usr/bin/env python3
def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**18

    for s in range(N):
        for e in range(N):
            time = 0
            for a, b in AB:
                time += abs(AB[s][0] - a) + abs(a - b) + abs(b - AB[e][1])

            ans = min(ans, time)
    
    return ans

print(main())
