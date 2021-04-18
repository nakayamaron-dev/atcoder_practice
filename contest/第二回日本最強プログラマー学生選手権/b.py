N, M = map(int,input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

ans_arr = list(A ^ B)
ans_arr.sort()

for idx, ans in enumerate(ans_arr):
    if idx == len(ans_arr):
        print(ans)
    else:
        print(ans, end=" ")

