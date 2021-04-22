#!/usr/bin/env python3
def main():
    S = input()
    
    if S[:12] == "WBWBWWBWBWBW":
        return "Do"
    
    if S[:12] == "WBWWBWBWBWWB":
        return "Re"
    
    if S[:12] == "WWBWBWBWWBWB":
        return "Mi"

    if S[:12] == "WBWBWBWWBWBW":
        return "Fa"
    
    if S[:12] == "WBWBWWBWBWWB":
        return "So"
    
    if S[:12] == "WBWWBWBWWBWB":
        return "La"
    
    if S[:12] == "WWBWBWWBWBWB":
        return "Si"
    
print(main())

# self AC
