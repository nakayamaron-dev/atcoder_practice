#!/usr/bin/env python3
n,m = list(map(int, input().split()))
 
ac = [0]*n
wa = [0]*(n+1)
pena = 0
 
for i in range(m):
  prob, state = input().split()
  prob = int(prob)-1
  
  if state == "AC" and ac[prob] == 0:
    ac[prob] = 1
    pena += wa[prob]
  elif state == "WA" and ac[prob] == 0:
    wa[prob] += 1
    
print(sum(ac), pena)

## AC
