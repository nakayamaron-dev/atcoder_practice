#!/usr/bin/env python3
N,M=map(int,input().split())
city=[]
#最後に並び替えるためにindexを振っておく。
for i in range(M):
    city.append(list(map(int,input().split()))+[i])

city=sorted(city)
id_num=[1]*N

for i in range(M):
    city_id = str(city[i][0]).zfill(6)
    order_id = str(id_num[city[i][0]-1]).zfill(6)
    city[i].append(city_id+order_id)
    id_num[city[i][0]-1]+=1

#答え出力用に再ソート
city=sorted(city,key=lambda x:x[2])

for i in range(M):
    print(city[i][3])

# not self AC
