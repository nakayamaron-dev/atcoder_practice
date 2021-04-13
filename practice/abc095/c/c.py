#!/usr/bin/env python3
A, B, AB, X, Y = map(int,input().split())

#A, Bをそれぞれの枚数分買うか、ABピザを少ない枚数分買う+α、ABピザを多い枚数分買う+α

#A, Bをそれぞれの枚数分買う.
ans1 = A*X + B*Y

# ABピザを少ない枚数分買う+α、ABピザを多い枚数分買う+α
if X > Y:
    ans2 = 2*AB*Y + A*(X-Y)
    ans3 = 2*AB*X
else:
    ans2 = 2*AB*X + B*(Y-X)
    ans3 = 2*AB*Y

ans = min(ans1, ans2, ans3)
print(ans)

# self AC 
# 簡単
