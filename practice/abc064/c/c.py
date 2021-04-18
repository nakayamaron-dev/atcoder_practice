#!/usr/bin/env python3
def get_color(n: int):
    if n < 400: return "gray"
    if n < 800: return "brown"
    if n < 1200: return "green"
    if n < 1600: return "light_blue"
    if n < 2000: return "blue"
    if n < 2400: return "yellow"
    if n < 2800: return "orange"
    if n < 3200: return "red"
    return "free"

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0, 0]
    colors = []
    colors_set = set()
    for a in A:
        colors.append(get_color(a))
        colors_set.add(get_color(a))

    if "free" in colors_set:
        if colors.count("free") == len(colors):
            ans[0] = 1
        else:
            ans[0] = len(colors_set) - 1
        ans[1] = len(colors_set) - 1 + colors.count("free")
    else:
        ans = [len(colors_set), len(colors_set)]
    
    return ans

print(*main())

# self AC
