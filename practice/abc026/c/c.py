#!/usr/bin/env python3
def main():
    N = int(input())

    B = [[] for _ in range(N+1)]
    for i in range(2, N+1):
        b = int(input())
        B[b].append(i)
    
    def rec(n: int):
        if not B[n]:
            return 1
        
        lst = [rec(i) for i in B[n]]
        return max(lst) + min(lst) + 1
    
    print(rec(1))

main()

# not self AC
# いい問題、再帰の勉強になる。
