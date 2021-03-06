N = int(input())
A = list(map(int, input().split()))

sq=0
s=0
for i in range(N):
    sq += A[i]**2
    s += A[i]
 
print(N*sq-s**2)

# 式展開すると、2乗の総和*N - 総和の２乗になる。