def main():
    N, A, X, Y = map(int,input().split())

    cost = min(N, A)*X + max(0, N-A)*Y

    return cost

print(main())