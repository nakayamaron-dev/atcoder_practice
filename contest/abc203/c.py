def main():
    N, K = map(int,input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    mura = 0

    for a, b in AB:
        dist = a - mura
        if dist > K:
            return mura + K
        else:
            mura += dist
            K += b - dist
    
    return mura + K

print(main())