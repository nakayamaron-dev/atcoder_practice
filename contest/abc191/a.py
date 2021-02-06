v, t, s, d = map(int,input().split())

start = v*t
end = s*v

if start <= d and d <= end:
    print('No')
else:
    print('Yes')

## AC