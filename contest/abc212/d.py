from heapq import heappop, heapify, heappush
def main():
    Q = int(input())
    bag = []
    heapify(bag)
    addNum = 0

    for _ in range(Q):
        q = list(map(int, input().split()))
        
        if q[0] == 1:
            heappush(bag, q[1] - addNum)
        elif q[0] == 2:
            addNum += q[1]
        else:
            print(heappop(bag) + addNum)
    
main()