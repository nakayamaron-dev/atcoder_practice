def get_max_num(num):
    arr = [int(char) for char in list(str(num))]
    return max(arr)

def calc_as_base_num(base_num, num):
    result = 0
    arr = [int(char) for char in list(str(num))]
    
    for idx, n in enumerate(reversed(arr)):
        result += n * (base_num ** idx)

    return result

def solve():
    X = int(input())
    M = int(input())
    d = get_max_num(X)
    n = 0
    cnt = 0

    while n <= M:
        cnt += 1
        n =  calc_as_base_num(d+cnt, X)

    return cnt - 1

print(solve())

