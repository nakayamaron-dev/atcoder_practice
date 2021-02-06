n, x = map(int,input().split())
a = list(map(int, input().split()))

ans = [i for i in a if i != x]

if len(ans) == 0:
    print('')
else:
    for idx, itm in enumerate(ans):
        if idx == len(ans)-1:
            print(itm)
        else:
            print(itm, end=' ')

## AC
