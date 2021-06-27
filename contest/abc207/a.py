def main():
    A, B, C = map(int,input().split())
    arr = [A, B, C]
    arr.sort(reverse=True)

    return arr[0] + arr[1]

print(main())