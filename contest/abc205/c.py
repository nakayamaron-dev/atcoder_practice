def main():
    A, B, C = map(int,input().split())

    if A >= 0 and B >= 0:
        if A < B: return "<"
        elif A == B: return "="
        else: return ">"
    elif A >= 0 and B < 0:
        if C % 2 == 0:
            if A < abs(B): return "<"
            elif A == abs(B): return "="
            else: return ">"
        else:
            return ">"
    elif A < 0 and B >= 0:
        if C % 2 == 0:
            if abs(A) < B: return "<"
            elif abs(A) == B: return "="
            else: return ">"
        else:
            return "<"
    else:
        if C % 2 == 0:
            if abs(A) < abs(B): return "<"
            elif abs(A) == abs(B): return "="
            else: return ">"
        else:
            if abs(A) < abs(B): return ">"
            elif abs(A) == abs(B): return "="
            else: return "<"

print(main())