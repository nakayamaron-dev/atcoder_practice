N = int(input())
AB = [list(map(int, input().split())) for l in range(N)]

def combinations_array(num_array, r):
    import itertools
    return list(itertools.combinations(num_array, r))

# 一人の社員で全てやるか、異なる2人で分担するか。

alone_work_time = []
for i in AB:
    alone_work_time.append(i[0]+i[1])

min_alone_work_time = min(alone_work_time)

comb = combinations_array([x for x in range(N)], 2)

min_time = 10**6
for itm1, itm2 in comb:
    time1 = max(AB[itm1][0], AB[itm2][1])
    time2 = max(AB[itm1][1], AB[itm2][0])

    time = min(time1, time2)

    if time < min_time:
        min_time = time

ans = min(min_alone_work_time, min_time)
print(ans)

