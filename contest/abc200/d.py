from collections import Counter
n = int(input())
a = list(map(int, input().split()))

# 制約が200以下なので全探索の可能性あり。
# mod 200が同じ組み合わせがあればYes, bとcは単一の要素でよい。
# ↑が存在しない場合、各要素の足し算の組み合わせで同じ値の組み合わせが作れるかどうかの問題
a = [itm % 200 for itm in a]
a.sort()
cnt = Counter(a)

if max(cnt.values()) > 1:
    ans = []
    for i in range(n):
        if a[i] == max(cnt.values()):
            ans.append(i)
    print("Yes")
    print(1, ans[0])
    print(1, ans[1])
else:
    for bit in range(2**n):
        Sum = 0
        for itm in a:
            if (bit>>itm) & 1:
                Sum += itm
                if cnt.get(Sum, "None") != "None":
