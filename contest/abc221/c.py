def main():
    N = list(input())
    ans = 0

    # 分け方全探索
    # 分けた後はそれぞれ最大値にする。
    for bit in range(1, 2**len(N)-1):
        tgt1 = []
        tgt2 = []
        for i in range(len(N)):
            if (bit >> i) & 1:
                tgt1.append(N[i])
            else:
                tgt2.append(N[i])

        tgt1.sort(reverse=True)
        tgt2.sort(reverse=True)

        num1 = int("".join(tgt1))
        num2 = int("".join(tgt2))

        ans = max(ans, num1*num2)

    return ans


print(main())
