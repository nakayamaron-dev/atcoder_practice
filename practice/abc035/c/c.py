#!/usr/bin/env python3
def main():
    N, Q = map(int,input().split())
    ans = [0]*N
    arr = [0]*(N+1)

    for i in range(Q):
        L, R = map(int,input().split())
        arr[L-1] += 1
        arr[R] -= 1
    
    cnt = 0
    for i in range(N):
        cnt += arr[i]
        ans[i] = cnt%2
    
    return "".join(map(str, ans[:N]))

print(main())

# not self AC
# いもす法をきちんと理解すれば解けそう。
