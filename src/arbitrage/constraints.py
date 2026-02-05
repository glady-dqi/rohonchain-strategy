"""Constraint builder for prediction market outcomes.
Example: Duke vs Cornell mutual-exclusion constraints.
"""
from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass
class Constraint:
    # A^T z >= b  (encoded as list of (coeffs, rhs))
    coeffs: Dict[str, float]
    rhs: float


def one_hot_constraints(prefix: str, outcomes: List[int]) -> List[Constraint]:
    # Sum z(prefix, outcomes) = 1  -> encoded as >=1 and <=1 (via -sum >= -1)
    coeffs = {f"{prefix}_{o}": 1.0 for o in outcomes}
    return [
        Constraint(coeffs=coeffs, rhs=1.0),
        Constraint(coeffs={k: -v for k, v in coeffs.items()}, rhs=-1.0)
    ]


def mutual_exclusion(prefix_a: str, wins_a: List[int], prefix_b: str, wins_b: List[int]) -> Constraint:
    coeffs = {f"{prefix_a}_{o}": 1.0 for o in wins_a}
    coeffs.update({f"{prefix_b}_{o}": 1.0 for o in wins_b})
    return Constraint(coeffs=coeffs, rhs=1.0)  # sum <= 1  -> encoded later
