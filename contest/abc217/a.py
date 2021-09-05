def main():
    S, T = input().split()
    arr = [S, T]
    arr.sort()

    if arr[0] == S:
        return "Yes"
    else:
        return "No"


print(main())
