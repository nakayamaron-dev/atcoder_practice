def main():
    X, Y = map(int,input().split())

    if X == Y:
        return X
    else:
        return 3 - X - Y


print(main())