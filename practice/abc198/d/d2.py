#!/usr/bin/env python3
import itertools
def main():
    s1 = [i for i in input()]
    s2 = [i for i in input()]
    s3 = [i for i in input()]
    sl = list(set(s1+s2+s3))

    if len(sl)>10 or (len(s3)-len(s1)>=2 and len(s3)-len(s2)>=2) or len(s3)<len(s1) or len(s3)<len(s2):
        print("UNSOLVABLE")
        exit()
    
    for ptn in itertools.permutations(range(10), len(sl)):
        dic = dict()

        for i in range(len(sl)):
            dic[sl[i]] = ptn[i]
        
        n1 = "".join([str(dic[itm]) for itm in s1])
        n2 = "".join([str(dic[itm]) for itm in s2])
        n3 = "".join([str(dic[itm]) for itm in s3])

        # 先頭が0の場合スキップ
        if n1[0] == "0" or n2[0] == "0" or n3[0] == "0":
            continue

        if int(n1) + int(n2) == int(n3):
            print(n1)
            print(n2)
            print(n3)
            exit()
    
    print("UNSOLVABLE")

main()
