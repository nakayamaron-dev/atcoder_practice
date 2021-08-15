from heapq import heappop, heapify, heappush
def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    stones = [False]*N
    Ts = sorted(range(len(T)), key=lambda k: T[k])

    for i in range(N):
        fromT = T[i]
        fromS = 0
        prev = 0

        while 1:
            if i == 0:
                fromS += S[-1]
                i = N-1
            else:
                fromS += S[i-1]
            
            prev += 1
            if fromS >= fromT:
                break
        





            




print(main())