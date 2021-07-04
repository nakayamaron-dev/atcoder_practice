def main():
    P = int(input())
    costs = [1]

    for i in range(2, 11):
        costs.append(costs[-1] * i)

    costs.sort(reverse=True)
    cnt = 0

    for itm in costs:
        cost = 0
        if itm <= P:
            while cost + itm <= P:
                cost += itm
                cnt += 1
        
            P -= cost

            if P == 0:
                return cnt

print(main())