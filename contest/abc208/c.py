def main():
    N, K = map(int,input().split())
    A = list(map(int, input().split()))
    AA = sorted(A).copy()
    dic = dict()

    for i in range(N):
        dic[AA[i]] = i+1
    
    print(dic)
    print(A)

    div = K // N
    amari = K % N

    for a in A:
        if dic[a] <= amari:
            print(div + 1)
        else:
            print(div)

main()