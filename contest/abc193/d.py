K = int(input())
S = input()
T = input()

def calc_point(s):
    num_arr = [int(cha) for cha in s]
    point = 0
    for i in range(1, 10):
        point += i * 10**num_arr.count(i)

    return point

def permutations_array(arr, r):
    import itertools
    return list(itertools.permutations(arr, r))

S_num_arr = [int(cha) for cha in S[:-1]]
T_num_arr = [int(cha) for cha in T[:-1]]
hand_cards = S_num_arr + T_num_arr
cards = []

for i in range(1, 10):
    for _ in range(K):
        cards.append(i)

for i in hand_cards:
    cards.remove(i)

T_point = 0
A_point = 0
T_win = 0
cnt = 0

for i, j in permutations_array(cards, 2):
    T_point = calc_point(T[:-1]+str(j))
    S_point = calc_point(S[:-1]+str(i))
    cnt += 1

    if T_point > S_point:
        T_win += 1

print(cnt)
print(T_win / cnt)

