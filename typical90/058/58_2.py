#!/usr/bin/env python3
def main():
    N, K = map(int,input().split())
    MAX = 10**5
    dic = dict()
    cache = [N]

    for i in range(MAX):
        N += sum(int(c) for c in str(N))
        N %= MAX

        if dic.get(N, "None") != "None":
            break
        else:
            dic[N] = 1
        
        cache.append(N)
    
    # loopに入る前の値を出力する場合
    if len(cache) > K:
        return cache[K]
    
    start = 0
    for i in range(len(cache)):
        if N == cache[i]:
            start = i
            break
    
    loop = len(cache) - start

    K -= start
    K %= loop
    K += start

    return cache[K]

print(main())