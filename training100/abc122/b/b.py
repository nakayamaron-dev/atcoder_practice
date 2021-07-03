#!/usr/bin/env python3
def main():
    S = input()
    sl = len(S)
    agct = ["A", "G", "C", "T"]
    ans = 0

    for i in range(sl):
        l = 0
        if S[i] not in agct: continue
        l += 1
        
        for j in range(i+1, sl):
            if S[j] not in agct: break

            l += 1
        ans = max(ans, l)
    
    return ans

print(main())
