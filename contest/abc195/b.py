A, B, W = map(int,input().split())
W = W*1000
ans = []

for i in range(1, W+1):
    avg = W / i
    if avg >= A and avg <= B:
        ans.append(i)

if len(ans) == 0:
    print("UNSATISFIABLE")
else:
    print(min(ans), max(ans))

    
