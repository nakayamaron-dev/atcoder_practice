N, S, D = map(int, input().split())
l = [list(map(int, input().split())) for l in range(N)]

ans = 'No'

for itm in l:
  if itm[0] < S:
    if itm[1] > D:
      ans = 'Yes'
print(ans)

## AC