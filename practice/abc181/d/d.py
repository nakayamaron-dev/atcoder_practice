#!/usr/bin/env python3
from collections import Counter
s = input()


def main():
    if len(s) <= 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            return 'Yes'
        else:
            return 'No'

    cnt = Counter(s)

    for i in range(104, 1000, 8):
        if not Counter(str(i)) - cnt:
            return 'Yes'

    return 'No'


print(main())

# Counterという便利機能
