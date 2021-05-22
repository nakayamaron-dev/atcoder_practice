#!/usr/bin/env python3
def main():
    S = input()
    ans = [1]*len(S)

    for i in range(len(S)-2):
        if S[i] == "R" and S[i+1] == "R":
            ans[i+2] += ans[i]
            ans[i] = 0
    
    for i in range(len(S)-1, 1, -1):
        if S[i] == "L" and S[i-1] == "L":
            ans[i-2] += ans[i]
            ans[i] = 0
    
    return ans

print(*main())

# not self AC
