from bisect import bisect_left
def main():
    N, Q = map(int,input().split())
    A = list(map(int, input().split()))
    B = [A[i]-i-1 for i in range(N)]

    for _ in range(Q):
        K = int(input())
        i = bisect_left(B, K)

        if i < N:
            print(A[i] + K - B[i] - 1)
        else:
            print(A[-1] + K - B[-1])

main()