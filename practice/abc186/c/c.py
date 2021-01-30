#!/usr/bin/env python3
n = int(input())
isSeven_list = []

def splitdigit(num_str):
    return list(map(int, num_str))

def isNum(num, num_array):
    return num in num_array

for i in range(n+1):
    array = splitdigit(str(i))
    oct_array = splitdigit(oct(i)[2:])

    if isNum(7, array) or isNum(7, oct_array):
        isSeven_list.append(i)

sevens = len(list(set(isSeven_list)))
print(n - sevens)

## AC






