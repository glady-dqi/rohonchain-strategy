"""Non-atomic execution risk model."""

def min_liquidity_cap(volumes):
    return min(volumes) if volumes else 0
