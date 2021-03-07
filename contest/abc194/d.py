N = int(input())
 
ans = 0
for i in range(1, N):
    ans += N / (N-i)
 
print(ans)

# Σi種類あるときに新が出るまでの期待値
# 確率：N-i / N
# 有効なのが来るまでカードを引く期待値は、有効なカードを引く確率の逆数になる。(知識)