def main():
    A, B = map(int,input().split())

    minval = A
    maxval = A * 6

    if minval <= B and B <= maxval:
        return "Yes"
    else:
        return "No"

print(main())