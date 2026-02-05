"""Frank–Wolfe with IP oracle placeholder.
"""
import numpy as np


def frank_wolfe(grad_fn, oracle_fn, init, iters=50):
    mu = np.array(init, dtype=float)
    for t in range(1, iters + 1):
        grad = grad_fn(mu)
        z = oracle_fn(grad)
        gamma = 2.0 / (t + 2)
        mu = (1 - gamma) * mu + gamma * z
    return mu
