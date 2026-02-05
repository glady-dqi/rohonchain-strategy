"""Bregman projection for LMSR (KL divergence).
"""
import numpy as np

def kl_div(mu, theta):
    mu = np.asarray(mu) + 1e-12
    theta = np.asarray(theta) + 1e-12
    return np.sum(mu * (np.log(mu) - np.log(theta)))
