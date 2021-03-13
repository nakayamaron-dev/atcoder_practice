N = int(input())

def get_digit_num(num):
    return len(str(num))

digit_num = get_digit_num(N)
ans = 0

if digit_num < 4:
    print(0)
else:
    for i in range(4, digit_num+1):
        comma_num = (i-1) // 3
        iter_num = 9 * 10 ** (i - 1)

        if i == digit_num:
            ans += comma_num * (N + 1 - 10 ** (i - 1))
        else:
            ans += comma_num * iter_num

    print(ans)
