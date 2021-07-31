from bisect import bisect_left,bisect_right
def main():
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 10**9 + 7

    for a in A:
        idx = bisect_left(B, a)
        
        if idx == 0:
            dim = abs(a - B[idx])
        elif idx == M:
            dim = abs(a - B[idx-1])
        else:
            dim = min(abs(a - B[idx]), abs(a - B[idx-1]))
        
        ans = min(ans, dim)
    
    return ans

print(main())