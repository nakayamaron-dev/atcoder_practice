#!/usr/bin/env python3
def main():
    N = int(input())
    acm1, acm2 = [0], [0]

    for _ in range(N):
        C, P = map(int,input().split())

        if C == 1:
            acm1.append(acm1[-1] + P)
            acm2.append(acm2[-1])
        else:
            acm2.append(acm2[-1] + P)
            acm1.append(acm1[-1])

    Q = int(input())
    for _ in range(Q):
        l, r = map(int,input().split())

        ans1 = acm1[r] - acm1[l-1]
        ans2 = acm2[r] - acm2[l-1]

        print(ans1, ans2)

main()
