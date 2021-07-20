#!/usr/bin/env python3
def main():
    A, B, C = map(int,input().split())

    if A < C ** B:
        return "Yes"
    else:
        return "No"

print(main())