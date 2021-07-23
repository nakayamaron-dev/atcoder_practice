#!/usr/bin/env python3
def shinsu(num, base):
    nine = ""
    while num > 0:
        nine += str(num % base)
        num //= base
    return int(nine[::-1])

def main():
    N, K = map(int,input().split())

    if N == 0: return 0

    for i in range(K):
        N = shinsu(int(str(N), 8), 9)

        c = ""
        for i in range(len(str(N))):
            if str(N)[i] == "8":
                c += "5"
            else:
                c += str(N)[i]
        
        N = int(c)
    
    return N

print(main())