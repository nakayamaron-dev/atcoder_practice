def num2alpha(num):
    if num <= 26:
        return chr(64+num)
    elif num % 26 == 0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num % 26)


def main():
    P = list(map(int, input().split()))
    ans = ""

    for p in P:
        ans += num2alpha(p).lower()

    return ans


print(main())
