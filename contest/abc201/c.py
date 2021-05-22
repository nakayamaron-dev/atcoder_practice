# S = input()
# maru = S.count("o")
# hatena = S.count("?")

# if maru > 4:
#     ans = 0
# else:
#     if maru == 4:
#         ans = 24
#     elif maru == 3:
#         ans = 24 * hatena + 36
#     elif maru == 2:
#         ans = 12 * (hatena**2) + 24 * hatena + 14
#     elif maru == 1:
#         ans = 4 * (hatena**3) + 6 * (hatena**2) + 4 * hatena + 1
#     else:
#         ans = hatena ** 4
    
# print(ans)

S = input()
ans = 0
for v in range(10000):
    v = str(v).zfill(4)
    res = 1
    for i, x in  enumerate(S):
        # 絶対に使っている数字なのに、暗証番号にない場合
        if x == "o" and str(i) not in v:
            res = 0
        
        # 絶対に使ってないのに、暗証番号にある場合
        elif x == "x" and str(i) in v:
            res = 0
            
    ans += res

print(ans)
