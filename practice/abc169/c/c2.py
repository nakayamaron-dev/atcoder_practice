#!/usr/bin/env python3
from decimal import Decimal
def main():
    a, b = map(Decimal,input().split())
    return (a*b*100) // 100

print(main())

# self AC
