from collections import deque


def main():
    N, M = map(int, input().split())
    poll = []

    for _ in range(M):
        k = int(input())
        A = deque(list(map(int, input().split())))
        poll.append(A)

    for i in range(N):


print(main())
