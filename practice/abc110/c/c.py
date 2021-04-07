#!/usr/bin/env python3
S = input()
T = input()

sd = {}
td = {}
for i in range(len(S)):
    t = T[i]
    s = S[i]

    if s in sd:
        if sd[s] != t:
            print("No")
            exit()
    
    if t in td:
        if td[t] != s:
            print("No")
            exit()
    
    sd[s] = t
    td[t] = s

print("Yes")

# not self AC
