import math
import copy
def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    CD = [list(map(int, input().split())) for _ in range(N)]
    dist_ab = 10**9+1
    CD.sort()

    for a, b in AB:
        if abs(a)+abs(b) < dist_ab:
            dist_ab = abs(a)+abs(b)
            near_ab = [a, b]
    
    for i in range(N):
        AB[i][0] -= near_ab[0]
        AB[i][1]-= near_ab[1]
    
    print(AB)

    #ABの各点を90, 180, 270, 360度全て回転させて一致するかどうか全探索
    for n in range(90, 361, 90):
        print(n)
        state = "Yes"
        rad = math.radians(n)
        ab_rot = []
        for a, b in AB:
            a_rot = int(a * math.cos(rad)) - int(b * math.sin(rad))
            b_rot = int(a * math.sin(rad)) + int(b * math.cos(rad))
            ab_rot.append([a_rot, b_rot])
            print(a_rot, b_rot)
        
        ab_rot.sort()
        print(ab_rot)
        for i in range(-100, 101):
            for j in range(-100, 101):
                tgt = copy.deepcopy(ab_rot)
                for k in range(len(ab_rot)):
                    tgt[k][0] += i
                    tgt[k][1] += j
                
                if n == 90 and i == 3 and j == 0:
                    print(tgt)
                    print(CD)
        
                if tgt == CD:
                    return "Yes"
    
    return "No"

print(main())