N = int(input())
S = str(N)
digits = len(S)
ans = 0

if digits == 1:
    print(0)
else:
    for i in range(2, digits+1, 2):
        # Nの桁数と同じ場合、どこまで満たすのか検証確かめる必要がある。
        if i == digits:
            div = i // 2
            # 前半が後半より大きい場合
            if int(S[0:div]) > int(S[div:]):
                ans += (int(S[0:div])-1) - 10**(i//2 - 1) + 1
            else:
                ans += (int(S[0:div])) - 10**(i//2 - 1) + 1
        else:
            ans += 9*10**(i//2 - 1)
        
    print(ans)