#!/usr/bin/env python3
from collections import deque
def main():
    N, K = map(int,input().split())
    S = input()

    q = deque()
    ans = ""

    for num, char in enumerate(S):

        # q[-1] > rate: qの末尾要素がrateより辞書順で大きい場合、末尾要素を削除する。
        while q and q[-1] > char:
            q.pop()
        
        q.append(char)

        # 残り文字数がKを下回ったら、先頭の要素を答えに追加する。
        if num >= N - K:
            ans += q.popleft()
    
    return ans

print(main())
