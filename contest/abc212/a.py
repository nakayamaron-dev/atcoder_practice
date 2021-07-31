def main():
    A, B = map(int,input().split())

    if B == 0:
        return "Gold"
    
    if A == 0:
        return "Silver"
    
    return "Alloy"

print(main())