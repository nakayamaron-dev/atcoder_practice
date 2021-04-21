#!/usr/bin/env python3
def main():
    S = input()
    ans = 0

    #ビット全探索
    for bit in range(2**(len(S)-1)):
        tmp = S[0]
        for i in range(len(S)-1):
            if bit & (1 << i):
                tmp += "+"
            
            tmp += S[i+1]
        
        ans += sum(map(int, tmp.split("+")))
    
    return ans

print(main())

# not self AC
# まだまだビット全探索が弱点
