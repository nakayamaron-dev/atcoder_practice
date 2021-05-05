#!/usr/bin/env python3
from collections import deque
def main():
    S = deque(list(input()))
    Q = int(input())

    rev_cnt = 0

    for _ in range(Q):
        query = list(map(str, input().split()))
        t = int(query[0])

        if len(query) != 1:
            f = int(query[1])
            c = query[2]

        if t == 1:
            rev_cnt += 1
        else:
            if f == 1:
                if rev_cnt % 2 == 0:
                    S.appendleft(c)
                else:
                    S.append(c)
            else:
                if rev_cnt % 2 == 0:
                    S.append(c)
                else:
                    S.appendleft(c)
    
    if rev_cnt % 2 == 1:
        S = reversed(S)
    
    return "".join(S)

print(main())

# self AC
