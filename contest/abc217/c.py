def main():
    N = int(input())
    P = list(map(int, input().split()))

    cache = dict()
    ans = []

    for i in range(N):
        cache[P[i]] = i + 1

    for i in range(1, N+1):
        ans.append(str(cache[i]))

    return " ".join(ans)


print(main())
