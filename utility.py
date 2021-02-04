# 階乗計算
def calc_factorial(n):
    import math
    return math.factorial(n)

# 順列総数計算
def calc_permutations_count(n, r):
    import math
    return math.factorial(n) // math.factorial(n - r)

# 組み合わせ総数計算
def calc_combinations_count(n, r):
    import math
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# 順列をリスト化
def permutations_array(num_array, r):
    import itertools
    return list(itertools.permutations(num_array, r))

# 組み合わせをリスト化
def combinations_array(num_array, r):
    import itertools
    return list(itertools.combinations(num_array, r))

# 約数列挙
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

# 数字を桁ごとにリスト化
def splitdigit(num_str):
    return list(map(int, num_str))

# mod計算
def calc_mod(n, mod):
    return n % mod

# 最大公約数
def my_gcd(*numbers):
    from functools import reduce
    return reduce(math.gcd, numbers)

# 最小公倍数
def calc_lm(*numbers):
    import math
    return int(a * b / math.gcd(a, b))

# 素因数分解
def prime_factorize(n: int) -> list:
    return_list = []
    while n % 2 == 0:
        return_list.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            return_list.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        return_list.append(n)
    return return_list

# 数字 → アルファベット変換
def num2alpha(num):
    if num<=26:
        return chr(64+num)
    elif num%26==0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num%26)
