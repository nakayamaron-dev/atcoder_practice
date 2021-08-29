def tosa_sum(a, l, n, k):
    return k * ((n * (a + l)) // 2)


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    second_idx = 0
    maxval = A[0]
    dim = 0
    ans = 0

    for i in range(1, N):
        if A[i-1] != A[i]:
            second_idx = i
            second_val = A[second_idx]
            break

    while K > 0:
        d = maxval - second_val
        ans += tosa_sum(second_val+1, maxval, d, second_idx, K)
        print(ans, second_val, maxval, second_idx)

        if second_idx >= N:
            maxval = 0
        else:
            maxval = A[second_idx]

        second_idx += 1

        if second_idx >= N:
            second_val = 0
        else:
            second_val = A[second_idx]

    return ans


print(main())
