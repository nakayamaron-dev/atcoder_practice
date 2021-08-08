#!/usr/bin/env python3
def main():
    A, B = map(int,input().split())

    for c in range(256):
        if A ^ c == B:
            return c

print(main())