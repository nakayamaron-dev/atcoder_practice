from collections import deque
from heapq import heappop, heapify, heappush


def main():
    Q = int(input())
    que = deque()
    h = []
    heapify(h)
    minval = 10**9 + 7
    flag = False

    for i in range(Q):
        q = list(map(int, input().split()))

        if q[0] == 1:
            que.append(q[1])
            heappush(h, q[1])

        elif q[0] == 2:
            if flag:
                print(heappop(h))
                flag = False
            else:
                print(que.popleft())

        elif q[0] == 3:
            flag = True


main()
