"""Sizing rule (modified Kelly placeholder)."""
import math

def modified_kelly(b, p):
    q = 1 - p
    if b <= 0: return 0
    return max(0.0, (b * p - q) / b * math.sqrt(p))
