import math
X, Y, Z = map(int,input().split())

taka = Y / X
sunu = math.ceil(Z * (Y / X))

print(sunu - 1)