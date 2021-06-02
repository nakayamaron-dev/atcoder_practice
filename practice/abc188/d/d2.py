#!/usr/bin/env python3
def main():
    N, C = map(int,input().split())

    # ai-1日目とai日目の間に料金がci円上がるイベントが起こる。
    # bi日目とbi+1日目の間に料金がci円下がるイベントが起こる。
    event = []
    for i in range(N):
        a, b, c = map(int,input().split())
        event.append((a-1, c))
        event.append((b, -c))
    
    event.sort()
    ans, fee, day = 0, 0, 0

    for x, y in event:
        # 各種サービスの合計利用料とプライム加入料C円の小さい方の金額を次のイベントまで支払う。
        ans += min(fee, C) * (x - day)

        # 日にちを更新
        day = x

        # 利用料を更新
        fee += y
    
    return ans

print(main())