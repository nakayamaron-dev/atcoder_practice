#!/usr/bin/env python3
from collections import Counter
def calc_score(counter: Counter):
    ans = 0
    for i in range(1, 10):
        ans += i * 10**(counter.get(str(i), 0))
    return ans

def use_card(arr: list, i, j):
    if i == j:
        if arr[i] > 1: return True
    else:
        if arr[i] > 0 and arr[j] > 0: return True
    return False

def main():
    K = int(input())
    S = input()[:-1]
    T = input()[:-1]
    cards = [K] * 9
    t_win = 0

    for c in S:
        cards[int(c)-1] -= 1

    for c in T:
        cards[int(c)-1] -= 1
    
    s_cnt = Counter(S)
    t_cnt = Counter(T)
    ptn = (9*K - 8) * (9*K - 9)

    for i in range(1, 10):
        for j in range(1, 10):
            s_cnt_tmp = s_cnt.copy()
            t_cnt_tmp = t_cnt.copy()
            # カードが残っていない場合はパス
            if use_card(cards, i-1, j-1) == False: continue

            s_cnt_tmp[str(i)] = s_cnt_tmp.get(str(i), 0) + 1
            t_cnt_tmp[str(j)] = t_cnt_tmp.get(str(j), 0) + 1
            
            s_score = calc_score(s_cnt_tmp)
            t_score = calc_score(t_cnt_tmp)

            if s_score > t_score:
                if i == j:
                    t_win += cards[i-1] * (cards[i-1] - 1)
                else:
                    t_win += cards[i-1] * cards[j-1]

    return t_win / ptn     

print(main())

# not self AC
# 惜しかった。
