s = input()
ans = 0
for i in range(len(s)-4):
    tgt = s[i:i+4]
    print(tgt)
    if tgt == "ZONe":
        ans += 1

print(ans)