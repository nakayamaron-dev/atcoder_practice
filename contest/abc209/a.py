def main():
    A, B = map(int,input().split())

    return max(B - A + 1, 0)

print(main())