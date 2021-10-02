def main():
    N = int(input())
    event = []

    for _ in range(N):
        A, B = map(int, input().split())
        event.append((A-1, 1))
        event.append((A+B-1, -1))

    event.sort()
    loginNum, day = 0, 0
    ans = [0] * (N+1)

    for x, y in event:
        ans[loginNum] += (x - day)
        day = x
        loginNum += y

    for i in range(1, len(ans)):
        if i == len(ans) - 1:
            print(ans[i])
        else:
            print(ans[i], end=" ")


main()
