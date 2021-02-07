#!/usr/bin/env python3
N, C = map(int,input().split())
event = []

# ai-1日目とai日目の間に料金がci円上がるイベントが起こる。
# bi日目とbi+1日目の間に料金がci円下がるイベントが起こる。
for i in range(N):
    a, b, c = map(int, input().split())
    a -= 1
    event.append((a, c))
    event.append((b, -c))

event.sort()
ans, fee, t = 0, 0, 0

for x, y in event:
    if x != t:
        ans += min(C, fee) * (x - t)
        t = x
    fee += y

print(ans)

## 再度取り組みたい。
