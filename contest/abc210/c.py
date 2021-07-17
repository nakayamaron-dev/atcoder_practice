from collections import Counter
def main():
    N, K = map(int,input().split())
    C = list(map(int, input().split()))

    if K == N:
        return len(set(C))
    
    
    cnt = Counter(C[:K])
    ans = len(cnt)
    
    for i in range(K, N):
        new = C[i]
        out = C[i-K]
        
        cnt[out] -= 1
        if cnt[out] == 0:
            cnt.pop(out)

        if cnt.get(new, 0) == 0:
            cnt[new] = 1
        else:
            cnt[new] += 1
        
        ans = max(ans, len(cnt))
    
    return ans

print(main())