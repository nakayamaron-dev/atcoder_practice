#!/usr/bin/env python3
N = int(input())

def mod3(n):
    return n % 3

digitArray = list(map(int, str(N)))
digitSum = sum(list(map(int, str(N))))

if mod3(digitSum) == 0:
    print(0)
elif mod3(digitSum) == 1:
    if len(digitArray) < 2:
        print(-1)
    else:
        # mod3=1のものがあればそれを取り除く。
        if 1 in map(mod3, digitArray):
            print(1)
        # mod3=1のものがなく、mod3=2のものが２つあればそれらを取り除く。
        else:
            if len(digitArray) < 3:
                print(-1)
            else:
                print(2)
else:
    if len(digitArray) < 2:
        print(-1)
    else:
        # mod3=2のものがあればそれを取り除く。
        if 2 in map(mod3, digitArray):
            print(1)
        # mod3=2のものがなく、mod3=1のものが２つあればそれらを取り除く。
        else:
            if len(digitArray) < 3:
                print(-1)
            else:
                print(2)

## self AC
