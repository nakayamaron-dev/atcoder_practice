from collections import defaultdict
N = int(input())
S = input()
Q = int(input())

arr1 = list(S[:N])
arr2 = list(S[N:])

for i in range(Q):
    T, A, B = map(int,input().split())

    if T == 1:
        if A > N:
            arr2[A-1-N], arr2[B-1-N] = arr2[B-1-N], arr2[A-1-N]
        elif B <= N:
            arr1[A-1], arr1[B-1] = arr1[B-1], arr1[A-1]
        else:
            arr1[A-1], arr2[B-1-N] = arr2[B-1-N], arr1[A-1]
    else:
        arr1, arr2 = arr2, arr1

print("".join(arr1+arr2))
