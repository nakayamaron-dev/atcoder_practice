def main():
    S = list(input())
    T = list(input())

    if S == T:
        return "Yes"

    for i in range(len(S)-1):
        tgt1 = S[i]
        tgt2 = S[i+1]
        S[i] = tgt2
        S[i+1] = tgt1

        if S == T:
            return "Yes"
        else:
            S[i] = tgt1
            S[i+1] = tgt2

    return "No"


print(main())
