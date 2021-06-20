def main():
    N = int(input())
    money = 0
    cnt = 1

    while money < N:
        money += cnt
        cnt += 1
    
    return cnt-1

print(main())