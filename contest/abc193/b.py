N = int(input())

min_price = 10**9 + 1

for i in range(N):
    A, P, X = map(int,input().split())
    zaiko = X - A
    price = P

    if zaiko > 0:
        min_price = min(min_price, price)

if min_price == 10**9 + 1:
    print(-1)
else:
    print(min_price)

