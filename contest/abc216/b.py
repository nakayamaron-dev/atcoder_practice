def main():
    N = int(input())
    name = set()

    for i in range(N):
        S, T = input().split()
        name.add((S, T))

    print(name, N, len(name))

    if len(name) == N:
        return "No"
    else:
        return "Yes"


print(main())
