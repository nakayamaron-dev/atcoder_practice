#!/usr/bin/env python3
from functools import lru_cache
a, b, c = map(int,input().split())

@lru_cache(maxsize=None)
def f(a, b, c):
    if a == 100 or b == 100 or c == 100:
        return 0

    s = a+b+c
    return f(a+1,b,c)*a/s + f(a,b+1,c)*b/s + f(a,b,c+1)*c/s + 1
            
print(f(a,b,c))

## lru_cacheはキャッシュを用いたプログラム高速化テクニック (主に再帰関数)
