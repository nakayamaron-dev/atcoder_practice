from collections import Counter, deque, defaultdict
from bisect import bisect_left, bisect_right
from decimal import Decimal
from heapq import heappop, heapify, heappush
import itertools

# 再帰上限を増やす
import sys
sys.setrecursionlimit(10**6)

# nで表現される集合に要素iが含まれるか判定してTrue/Falseを返す関数


def has_bit(n, i):
    return (n & (1 << i) > 0)

# print()の便利版


def chkprint(*args):
    from inspect import currentframe
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg), '???')+' = '+repr(arg) for arg in args))

# 配列の要素数列挙


def arr_counter(arr):
    from collections import Counter
    return Counter(arr)

# 配列で最も多い要素順に出力


def counter_most_common(arr):
    from collections import Counter
    return Counter(arr).most_common()

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
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# 非常に大きい数のnCrを計算する必要がある場合


def cmb(n, r, mod):
    x, y = 1, 1
    for i in range(r):
        x = x*(n-i) % mod
        y = y*(i+1) % mod

    # yで割ることと、pow(y, mod-2, mod)を掛けることは同義 (フェルマーの小定理)
    return x * pow(y, mod-2, mod) % mod

# 順列をリスト化


def permutations_array(arr, r):
    import itertools
    return list(itertools.permutations(arr, r))

# 組み合わせをリスト化


def combinations_array(num_array, r):
    import itertools
    return list(itertools.combinations(num_array, r))

# 重複ありで組み合わせをリスト化


def combinations_with_replacement(arr, n):
    import itertools
    return list(itertools.combinations_with_replacement(arr, n))

# 0,1の組み合わせ


def iter_product(arr, n):
    import itertools
    return list(itertools.product(arr, repeat=n))

# 約数列挙


def get_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

# 公約数を求める


def cf(x1, x2):
    cf = []
    for i in range(2, min(x1, x2)+1):
        if x1 % i == 0 and x2 % i == 0:
            cf.append(i)
    return cf

# 数字を桁ごとにリスト化


def splitdigit(num):
    return list(map(int, str(num)))

# 桁数


def digit_num(num):
    return len(str(num))

# mod計算


def calc_mod(n, mod):
    return n % mod

# 最大公約数


def gcd(*numbers):
    import math
    from functools import reduce
    return reduce(math.gcd, numbers)

# 最小公倍数


def lm(a: int, b: int):
    import math
    return (a * b) // math.gcd(a, b)

# 素因数分解


def prime_factorize(n: int) -> list:
    p = []
    while n % 2 == 0:
        p.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            p.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        p.append(n)
    return p

# 数字 → アルファベット変換


def num2alpha(num):
    if num <= 26:
        return chr(64+num)
    elif num % 26 == 0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num % 26)

# 素数判定


def is_prime(n):
    import math
    if n == 1:
        return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

# 素数列挙


def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


# """nを素因数分解"""
# """2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr

# 10進数をn進数に変換する。 (str)


def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)


def shinsu(num, base):
    nine = ""
    while num > 0:
        nine += str(num % base)
        num //= base
    return int(nine[::-1])

# 累積和配列


def prefix_sum(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

# 座標圧縮


def compress(arr):
    return {e: i for i, e in enumerate(sorted(set(arr)))}

# DFSサンプル


def dfs(pre, cur):
    for i in g[cur]:
        if i != pre:
            ans[i] += ans[cur]
            dfs(cur, i)

# 連番のxor計算


def XorSerial(n):
    if n % 2 == 0:
        return ((n//2) % 2) ^ n
    else:
        return (n//2) % 2


# 座標回転
def rotation(point, degree):
    import math
    cos = math.cos(math.radians(degree))
    sin = math.sin(math.radians(degree))
    x = round(point[0] * cos - point[1] * sin, 2)
    y = round(point[0] * sin + point[1] * cos, 2)

    return (x, y)
