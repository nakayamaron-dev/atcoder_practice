N = int(input())

ST = []
for _ in range(N):
    S, T = input().split()
    T = int(T)
    ST.append([S, T])

ST.sort(key=lambda x: x[1], reverse=True)

print(ST[1][0])