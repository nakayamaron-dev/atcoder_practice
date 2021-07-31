def main():
    X = input()
    ans = False

    if len(set(X)) == 1:
        return "Weak"
    
    for i in range(3):
        cur = int(X[i])
        nxt = int(X[i+1])
        sp = True

        if cur == 9 and nxt == 0:
            sp = False

        if cur + 1 != nxt and sp:
            ans = True
    
    return "Strong" if ans else "Weak"

print(main())