#!/usr/bin/env python3
n = int(input())
l = [str(input()) for _ in range(n)]
exclamation_list = []
nonexclamation_list = []

# !の有無でリスト分ける
for i in l:
    if i[0] == '!':
        exclamation_list.append(i[1:])
    else:
        nonexclamation_list.append(i)

duplicate = set(exclamation_list) & set(nonexclamation_list)

if len(duplicate) == 0:
    print('satisfiable')
else:
    print(list(duplicate)[0])

## AC