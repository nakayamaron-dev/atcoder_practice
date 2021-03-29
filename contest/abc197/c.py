N = int(input())
A = list(map(int, input().split()))
ans = float("inf")

#bit全探索
for i in range(2**(N-1)):
    or_num = 0
    xor_num = 0

    for j in range(N):
        or_num |= A[j]

        # 仕切りがある場合、xorを計算し、orを0に戻す
        if (i >> j) & 1:
            xor_num ^= or_num
            or_num = 0

    xor_num ^= or_num
    ans = min(xor_num, ans)

print(ans)