from collections import Counter
n = int(input())
a = list(map(int, input().split()))

#引き算だからmod 200が同じ数の個数
a = [itm % 200 for itm in a]
cnt = Counter(a)

ans = 0
for val in cnt.values():
    ans += val * (val-1) // 2

print(ans)