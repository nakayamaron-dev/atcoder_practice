def main():
    S = [input() for _ in range(4)]

    S = set(S)

    if len(S) == 4:
        return "Yes"
    else:
        return "No"

print(main())