#!/usr/bin/env python3
def main():
    S = input()

    while len(S) > 0:
        if S[-5:] == "dream" or S[-5:] == "erase":
            S = S[:-5]
        elif S[-6:] == "eraser":
            S = S[:-6]
        elif S[-7:] == "dreamer":
            S = S[:-7]
        else:
            return "NO"
    
    if len(S) == 0:
        return "YES"
    else:
        return "NO"

print(main())

# not self AC
# 逆順にするアイデアが思いつかなかった。
