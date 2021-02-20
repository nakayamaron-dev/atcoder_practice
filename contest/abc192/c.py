N, K = map(int,input().split())

def g2(num):
    arr = [int(char) for char in list(str(num))]
    arr.sort()
    arr = [str(char) for char in arr]

    return int("".join(arr))

def g1(num):
    arr = [int(char) for char in list(str(num))]
    arr.sort(reverse=True)
    arr = [str(char) for char in arr]

    return int("".join(arr))

def f(num):
    return g1(num) - g2(num)

def solve():
    Val = N
    for _ in range(K):
        Val = f(Val)
    
    return Val

print(solve())
        



