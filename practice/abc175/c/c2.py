#!/usr/bin/env python3
# 方針
# まずXから0に向けてできるだけ移動させる。
# 0をまたぐと残りは行ったり来たりを繰り返す。

X, K, D = map(int,input().split())

# 正に統一する。
X = abs(X)

cnt = X // D
mod = X % D

# 0をまたげない場合
if cnt >= K:
    print(X - D*K)
# 0をまたげる場合
else:
    if (K - cnt) % 2 == 1:
        print(abs(X - (cnt+1)*D))
    else:
        print(abs(X - cnt*D))

## not self AC
