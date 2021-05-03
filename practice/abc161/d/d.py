#!/usr/bin/env python3
from collections import deque
def main():
    k = int(input())
    q = deque(range(1, 10))

    for i in range(k):
        x = q.popleft()

        if x%10 != 0:
            q.append(10*x + (x%10) - 1)
        
        q.append(10*x + (x%10))

        if x%10 != 9:
            q.append(10*x + (x%10) + 1)

    return x

print(main())
    
# not self AC
# またdequeの問題。ルンルン数の規則に注目して末尾に加える数字を考える。
