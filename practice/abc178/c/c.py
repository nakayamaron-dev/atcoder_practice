#!/usr/bin/env python3
import math
n = int(input())

# 0が存在しない：9**n
# 9が存在しない：9**n
# 0と9が存在しない：8**n
# 0か9が少なくとも1つ存在しない：9**n + 9**n - 8**n

ans = 10**n - 9**n -9**n + 8**n
print(ans % (10**9 + 7))

## AC
