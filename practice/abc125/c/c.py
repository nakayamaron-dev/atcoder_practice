def my_gcd(*numbers):
    import math
    from functools import reduce
    return reduce(math.gcd, numbers)

#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))
L = [0]
R = [0]
 
for i in range(N):
    L.append(my_gcd(L[i], A[i]))
    R.append(my_gcd(R[i], A[N-1-i]))

R = R[::-1]
ans = []
for i in range(N):
    ans.append(my_gcd(L[i], R[i+1]))
    
print(max(ans))

# not self AC
