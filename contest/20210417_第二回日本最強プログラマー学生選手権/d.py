N, P = map(int,input().split())
mod = 10**9 + 7
ans = (P-1) * pow(P-2, N-1, mod)

# ans = (P-1) * (P-2)**(N-1) % (10**9 + 7)
print(ans)
