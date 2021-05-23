def main():
    S = input()
    S = list(S[::-1])

    for i in range(len(S)):
        if S[i] == "6":
            S[i] = "9"
        elif S[i] == "9":
            S[i] = "6"
    
    return "".join(S)

print(main())