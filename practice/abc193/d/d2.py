#!/usr/bin/env python3
from collections import Counter
def score(cnt: dict):
    score = 0
    for i in range(1, 10):
        score += i * (10 ** cnt.get(str(i), 0))
    return score

def use_card(arr, i, j):
    if i == j:
        return True if arr[i] > 1 else False
    else:
        return True if arr[i] > 0 and arr[j] > 0 else False

def main():
    K = int(input())
    S = input()[:-1]
    T = input()[:-1]
    cards = [K] * 9
    t_win = 0
    all_ptn = (9*K - 8) * (9*K - 9)

    for s, t in zip(S, T):
        cards[int(s)-1] -= 1
        cards[int(t)-1] -= 1

    for i in range(1, 10):
        for j in range(1, 10):
            s_cnt = Counter(S)
            t_cnt = Counter(T)

            if use_card(cards, i-1, j-1) == False: continue

            s_cnt[str(i)] = s_cnt.get(str(i), 0) + 1
            t_cnt[str(j)] = t_cnt.get(str(j), 0) + 1

            if score(s_cnt) > score(t_cnt):
                if i == j:
                    t_win += cards[i-1] * (cards[i-1] - 1)
                else:
                    t_win += cards[i-1] * cards[j-1]
    
    return t_win / all_ptn
    
print(main())
