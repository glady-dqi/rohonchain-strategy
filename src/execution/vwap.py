"""VWAP calculation for execution modeling."""

def vwap(trades):
    # trades = list of (price, volume)
    num = sum(p * v for p, v in trades)
    den = sum(v for _, v in trades)
    return num / den if den else None
