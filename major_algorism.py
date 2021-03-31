#bit全探索
def all_bit_explore(N: int):
    #1をN左シフトする。(2**Nの全探索)
    for i in range(1 << N):
        cond = [0]*N
        for j in range(N):
            #iをj右シフトする。(1の位が0か1か判定する。)
            if (i>>j) & 1:
                cond[j] = 1
        
        print(cond)

def all_bit_explore2(N: int):
    from itertools import product
    for p in product((0, 1), repeat=N):
        print(p)

#二分探索
def binary_search(arr: [int], i: int):
    # arr: 探索元の配列
    # i: 探索する値
    from bisect import bisect_right
    idx = bisect_right(arr, i)
    if arr[idx-1] != i:
        return False

    return True

#幅優先探索(BFS)




if __name__ == '__main__':
    print("##########bit全探索##########")
    all_bit_explore(3)
    print("##########bit全探索2##########")
    all_bit_explore2(3)
    print("##########二分探索##########")
    print(binary_search([1,3,5,6,7,10], 7))

    