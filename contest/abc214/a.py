def main():
    N = int(input())

    if N >= 212:
        return 8
    
    if N >= 126:
        return 6
    
    return 4

print(main())