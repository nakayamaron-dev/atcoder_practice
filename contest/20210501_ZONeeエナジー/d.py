from collections import deque
S = input()
T = deque()
rev = 0
for s in S:
    if s == "R":
        rev += 1
    else:
        if rev % 2 == 1:
            if T and T[0] == s:
                T.popleft()
            else:
                T.appendleft(s)
        else:
            if T and T[-1] == s:
                T.pop()
            else:
                T.append(s)

if rev % 2 == 1:
    T = reversed(T)

print("".join(T))

# not self AC
# ロジックはできていた。dequeを使っていればself AC