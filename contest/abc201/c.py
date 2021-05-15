S = input()

maru = S.count("o")
batu = S.count("x")
hatena = S.count("?")

if maru > 4:
    ans = 0
else:
    if maru == 4:
        ans = 24
    elif maru == 3:
        ans = 24 * hatena + 36
    elif maru == 2:
        ans = 12 * (hatena**2) + 24 * hatena + 14
    elif maru == 1:
        ans = 4 * (hatena**3) + 6 * (hatena**2) +4 * hatena + 1
    else:
        ans = hatena ** 4
    
print(ans)