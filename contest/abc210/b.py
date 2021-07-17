def main():
    N = int(input())
    S = input()

    for idx, s in enumerate(S):
        if s == "1":
            if idx % 2 == 0:
                return "Takahashi"
            else:
                return "Aoki"

print(main())