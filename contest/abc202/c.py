from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    cnt = Counter(A)

    for c in C:
        b = B[c-1]
        ans += cnt.get(b, 0)
    
    return ans

print(main())