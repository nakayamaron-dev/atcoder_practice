A = list(map(int, input().split()))
A.sort()

ans1 = A[1] - A[0]
ans2 = A[2] - A[1]

if ans1 == ans2:
    print("Yes")
else:
    print("No")