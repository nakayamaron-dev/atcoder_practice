def main():
    S, T = map(int,input().split())
    ans = 0

    for a in range(101):
        for b in range(101):
            for c in range(101):
                SUM = a+b+c
                MUL = a*b*c

                if SUM <= S and MUL <= T:
                    ans += 1
    
    return ans


print(main())