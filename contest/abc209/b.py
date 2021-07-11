def main():
    N, X = map(int,input().split())
    A = list(map(int, input().split()))

    nebiki = N // 2

    if sum(A) - nebiki <= X:
        return "Yes"
    else:
        return "No"

print(main())