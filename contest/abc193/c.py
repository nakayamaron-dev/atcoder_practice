N = int(input())

except_list = set()
a = 2

for _ in range(2, int(pow(N, 1/2))+1):
    b = 2
    if a in except_list:
        a += 1
    else:
        while a**b <= N:
            if a**b <= N :
                except_list.add(a**b)
            
            b += 1
            
        a += 1

print(N - len(except_list))