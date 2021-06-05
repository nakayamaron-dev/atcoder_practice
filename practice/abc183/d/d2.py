#!/usr/bin/env python3
def main():
    N, W = map(int,input().split())

    plan = []
    for i in range(N):
        s, t, p = map(int,input().split())
        plan.append([s, p])
        plan.append([t, -p])
    
    plan.sort()
    water = 0
    for s, p in plan:
        water += p

        if water > W:
            return "No"

    return "Yes" 

print(main())

# S分にP増え、T分にP減るイベントと考える。
