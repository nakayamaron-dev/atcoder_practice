S = input()
SR = S[::-1]
zero_cnt = 0

for itm in SR:
    if itm == "0":
        zero_cnt += 1
    else:
        break

add_zero = "0" * zero_cnt
S_add = add_zero + S
SR_add = S_add[::-1]

if S_add == SR_add:
    print("Yes")
else:
    print("No")

