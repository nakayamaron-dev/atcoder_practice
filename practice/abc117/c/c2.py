#!/usr/bin/env python3
def main():
    n, m = map(int,input().split())
    x = list(map(int, input().split()))
    x.sort()
    dim = []

    for i in range(m-1):
        dim.append(x[i+1]-x[i])
    
    dim.sort(reverse=True)
    
    return sum(dim[n-1:])

print(main())

# self AC
# コマの数だけ距離が遠い区間を削除できるという考え方。
