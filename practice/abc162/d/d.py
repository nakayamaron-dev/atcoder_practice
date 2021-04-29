#!/usr/bin/env python3
# 全探索するとTLEになる。
def main():
    n = int(input())
    s = input()
    ans = s.count("R") * s.count("G") * s.count("B")

    for i in range(n-1):
        for j in range(i+1, n):
            k = 2 * j - i

            if k < n:
                if s[i]!=s[j] and s[j]!=s[k] and s[k]!=s[i]:
                    ans -= 1
    
    return ans

print(main())

# not self AC
# 惜しかった。
    