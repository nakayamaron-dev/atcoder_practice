X = int(input())

def solve():
    cnt = 0
    for _ in range(100):
        X += 1
        cnt += 1
        if X % 100 == 0:
            break

    return cnt

print(solve())