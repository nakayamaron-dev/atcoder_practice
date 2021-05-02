#!/usr/bin/env python3
def main():
    n = int(input())
    h = list(map(int, input().split()))

    ans = 0
    while len(h) > 0:
        if h[0] == 0:
            h.pop(0)
            continue

        for i in range(len(h)):
            if h[i] > 0:
                h[i] -= 1
            else:
                break
        
        ans += 1
    
    return ans

print(main())

# not self AC
# 伸ばすべき高さが全ての花に対して1以上ならば、全ての花に水をやる。
# ある花xをもはや伸ばす必要がないならば、花1~x-1と花x+1~Nについて最小手数を別々に求めて、それらの必要手数を合計する。
