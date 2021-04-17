#!/usr/bin/env python3
import re
def main():
    S = input().replace("?", ".")
    T = input()

    for i in range(len(S)-len(T), -1, -1):
        if re.match(S[i:i+len(T)], T):
            S = S.replace(".","a")
            return S[:i]+T+S[i+len(T):]
    
    return "UNRESTORABLE"

print(main())

# not self AC
# 正規表現だと、matchだと"."は全て同じという認識になる。
