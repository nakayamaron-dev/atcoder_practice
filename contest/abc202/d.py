def calc_combinations_count(n, r):
    import math
    if n < r:return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    A, B, K = map(int,input().split())
    acm = 0
    ans = []

    # 先頭の文字から順番に決めていく。
    for _ in range(A+B):
        # aが無ければ自動的にbになる。
        if not A:
            ans.append("b")
        else:
            # 先頭の文字をaと過程し、先頭以降の文字列の総数を計算する。
            cnt = calc_combinations_count(A+B-1, A-1)
            
            if acm + cnt >= K:
                A -= 1
                ans.append("a")
            # どのパターンでもまだK番目にならないため、先頭文字としてbを選ぶ。
            else:
                acm += cnt
                B -= 1
                ans.append("b")
    
    return "".join(ans)

print(main())