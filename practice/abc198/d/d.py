#!/usr/bin/env python3
import itertools
s1 = [i for i in input()]
s2 = [i for i in input()]
s3 = [i for i in input()]
sl = list(set(s1+s2+s3))

# 11種類より多い場合、あり得ないので終了
if len(sl)>10 or (len(s3)-len(s1)>=2 and len(s3)-len(s2)>=2) or len(s3)<len(s1) or len(s3)<len(s2):
	print('UNSOLVABLE')
	exit()

# 全探索
for per in itertools.permutations(range(10),len(sl)):
	ndict = dict()
	for i in range(len(sl)):
		ndict[sl[i]] = per[i]
    
    # 先頭が0の場合、スキップする。
	if ndict[s1[0]]==0 or ndict[s2[0]]==0 or ndict[s3[0]]==0:
		continue

	n1 = ''.join([str(ndict[s]) for s in s1])
	n2 = ''.join([str(ndict[s]) for s in s2])
	n3 = ''.join([str(ndict[s]) for s in s3])
    
	if int(n1)+int(n2)==int(n3):
		print(n1)
		print(n2)
		print(n3)
		break
else:
	print('UNSOLVABLE')
