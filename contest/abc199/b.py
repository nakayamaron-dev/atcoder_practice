N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = set()

for i in range(N):
    tgt = set(range(A[i], B[i]+1))

    if i == 0:
        ans = tgt
    else:
        ans = ans & tgt

print(len(ans))
