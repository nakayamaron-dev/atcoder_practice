from bisect import bisect_left


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    # B[i]：Aのi番目の要素以下の数において、Aに含まれない正の整数の個数を格納した配列
    B = [A[i]-i-1 for i in range(N)]

    for _ in range(Q):
        K = int(input())
        i = bisect_left(B, K)

        if i < N:
            print((A[i] - 1) - (B[i] - K))
        else:
            print(A[-1] + K - B[-1])


main()
