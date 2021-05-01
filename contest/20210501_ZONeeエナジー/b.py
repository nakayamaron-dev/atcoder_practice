N, D, H = map(int,input().split())
DH = [list(map(int, input().split())) for _ in range(N)]
lines = []

for d, h in DH:
    slope = (H-h) / (D-d)
    intercept = H - slope*D
    lines.append([slope, intercept])

lines.sort()

if lines[0][1] <= 0:
    print(0)
else:
    print(lines[0][1])

