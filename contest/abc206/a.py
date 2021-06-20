def main():
    N = int(input())
    k = 1.08

    if int(N*k) > 206:
        return ":("
    
    if int(N*k) == 206:
        return "so-so"
    
    if int(N*k) < 206:
        return "Yay!"

print(main())