A, B = map(int,input().split())

nyuko = A+B
nyusi = B

if nyuko >= 15 and nyusi >= 8:
    print(1)
elif nyuko >= 10 and nyusi >= 3:
    print(2)
elif nyuko >= 3:
    print(3)
else:
    print(4)