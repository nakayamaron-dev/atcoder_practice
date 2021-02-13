#!/usr/bin/env python3
N, M = map(int,input().split())

print(pow(10, N, M*M)//M % M)

# 安直にすると10**Nが大きすぎてTLEになる。なのでM**2のmodで計算する必要がある。