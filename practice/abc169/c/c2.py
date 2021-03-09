#!/usr/bin/env python3
from decimal import Decimal
A, B = map(Decimal,input().split())

def main():
    return (A*B*100) // 100

print(main())

## not self AC