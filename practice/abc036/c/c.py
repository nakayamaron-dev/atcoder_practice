#!/usr/bin/env python3
def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A_sort = sorted(A)
    dic = {}
    cnt = 0

    for i in range(N):
        if dic.get(A_sort[i], "None") == "None":
            dic[A_sort[i]] = cnt
            cnt += 1
    
    for i in range(N):
        print(dic[A[i]])

main()

# self AC
