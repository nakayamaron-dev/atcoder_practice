import math
import itertools

# 階乗計算
def calc_factorial(n):
    return math.factorial(n)

# 順列総数計算
def calc_permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

# 組み合わせ総数計算
def calc_combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# 順列をリスト化
def permutations_array(num_array, r):
    return list(itertools.permutations(num_array, r))

# 組み合わせをリスト化
def combinations_array(num_array, r):
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
