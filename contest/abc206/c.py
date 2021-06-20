from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0

    cnt = Counter(A)
    
    for i in range(N):
        tgt = A[i]
        ans += N - cnt[tgt]

        cnt[tgt] -= 1
        N -= 1
    
    return ans

print(main())