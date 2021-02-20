
def solve():
    S = input()
    for idx, char in enumerate(S):
        if idx % 2 == 0:
            if char.isupper():
                return 'No'
        else:
            if char.islower():
                return 'No'
    
    return 'Yes'

print(solve())

