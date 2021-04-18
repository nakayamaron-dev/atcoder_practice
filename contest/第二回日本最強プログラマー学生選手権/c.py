A, B = map(int,input().split())
ans = B - A

for i in range(ans, 0, -1):
    if (A / ans).is_integer():
        a = A // ans
    else:
        a = A // ans + 1

    b = a + 1

    if ans * b <= B:
        print(ans)
        exit()
    else:
        ans -= 1
