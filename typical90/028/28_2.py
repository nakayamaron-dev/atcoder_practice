#!/usr/bin/env python3
def main():
    N = int(input())
    MAX = 1002
    mas = [[0] * MAX for _ in range(MAX)]

    for _ in range(N):
        lx, ly, rx, ry = map(int,input().split())
        mas[lx][ly] += 1
        mas[rx][ry] += 1
        mas[lx][ry] -= 1
        mas[rx][ly] -= 1
    
    # y方向に累積和
    for x in range(MAX):
        for y in range(MAX-1):
            mas[x][y+1] += mas[x][y]
    
    # x方向に累積和
    for x in range(MAX-1):
        for y in range(MAX):
            mas[x+1][y] += mas[x][y]
    
    ans = [0] * (N+1)
    for x in range(MAX):
        for y in range(MAX):
            ans[mas[x][y]] += 1
    
    for k in range(1, N+1):
        print(ans[k])

main()