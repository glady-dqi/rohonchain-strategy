"""Arbitrage detection using linear constraints / IP.
This is a research scaffold; plug in market data to build z and constraints.
"""
from typing import List
from .constraints import Constraint


def violates_constraints(z: dict, constraints: List[Constraint]) -> bool:
    for c in constraints:
        lhs = sum(z.get(k, 0.0) * v for k, v in c.coeffs.items())
        if lhs < c.rhs - 1e-9:
            return True
    return False
