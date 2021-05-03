#!/usr/bin/env python3
def main():
    n = int(input())
    c = list(map(int, input().split()))
    q = int(input())
    ans, s, z = 0, 0, 0
    min_s = 10**9
    min_z = 10**9

    for i in range(n):
        if i % 2 == 0:
            min_s = min(min_s, c[i])
        else:
            min_z = min(min_z, c[i])

    for _ in range(q):
        query =  list(map(int, input().split()))
        
        if query[0] == 1:
            x = query[1] - 1
            a = query[2]

            if x % 2 == 0:
                card_x = c[x] - z - s
            else:
                card_x = c[x] - z
            
            if card_x >= a:
                c[x] -= a
                ans += a

                if x % 2 == 0:
                    min_s = min(min_s, c[x])
                else:
                    min_z = min(min_z, c[x])

        elif query[0] == 2:
            a = query[1]
            if min_s - s - z >= a:
                s += a
        else:
            a = query[1]
            if min(min_s - s - z, min_z - z) >= a:
                z += a
    
    for i in range(n):
        if i % 2 == 0:
            ans += s
        ans += z
    
    return ans

print(main())
        
# not self AC
