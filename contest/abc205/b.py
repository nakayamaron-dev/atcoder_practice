def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = set(A)

    if len(A) == N:
        return "Yes"
    else:
        return "No"

print(main())