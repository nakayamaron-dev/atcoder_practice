S1 = input()
S2 = input()
S3 = input()
len_s1 = len(S1)
len_s2 = len(S2) 
len_s3 = len(S3)
arr = [1,2,3,4,5,6,7,8,9]

def permutations_array(arr, r):
    import itertools
    return list(itertools.permutations(arr, r))

str_uni = list(set(S1+S2+S3))

if len(str_uni) > 10:
    print("UNSOLVABLE")
    exit()

nums = permutations_array(arr, len(str_uni))

for ptn in nums:
    dic = {}
    for idx, itm in enumerate(str_uni):
        dic[itm] = str(ptn[idx])
    
    n1 = int(S1.translate(str.maketrans(dic)))
    n2 = int(S2.translate(str.maketrans(dic)))
    n3 = int(S3.translate(str.maketrans(dic)))

    if len(str(n1)) == len(S1) and len(str(n2)) == len(S2) and len(str(n3)) == len(S3):
        if n1 + n2 == n3:
            print(n1)
            print(n2)
            print(n3)
            exit()

print("UNSOLVABLE")