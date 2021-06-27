def main():
    A, B, C, D = map(int,input().split())

    if B / C >= D:
        return -1
    
    lb = A
    red = 0
    ans = 0
    while lb > D * red:
        red += C
        lb += B
        ans += 1
    
    return ans

print(main())
