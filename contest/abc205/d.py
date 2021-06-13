from bisect import bisect_left,bisect_right
def main():
    N, Q = map(int,input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)

    arr = [0]
    
    for i in range(1, N+1):
        dim = A[i] - A[i-1] -1
        arr.append(arr[i-1] + dim)
    
    arr.pop(0)
    A.pop(0)
    maxarr = max(arr)
    minarr = min(arr)
    
    for q in range(Q):
        K = int(input())

        if K > maxarr:
            print(K + N)
        elif K <= minarr:
            print(K)
        else:
            idx = bisect_left(arr, K)
            print(A[idx]-1)

main()