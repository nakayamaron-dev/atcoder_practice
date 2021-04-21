#!/usr/bin/env python3
def main():
    S = input()
    ans = 0

    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            ans += 1
    
    return ans

print(main())

# self AC